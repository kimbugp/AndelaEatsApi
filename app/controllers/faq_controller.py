from app.controllers.base_controller import BaseController
from app.repositories.faq_repo import FaqRepo
from sqlalchemy.exc import DataError
from app.utils.enums import FaqCategoryType
from datetime import datetime


class FaqController(BaseController):
    def __init__(self, request):
        BaseController.__init__(self, request)
        self.faq_repo = FaqRepo()

    def list_faqs(self, **kwargs):

        for name, val in kwargs.items():

            if name.endswith('ted_at'):
                try:
                    kwargs.__setitem__(name, datetime.strptime(kwargs.get(name), '%Y-%m-%d'))
                except Exception:
                    return self.handle_response(
                        f'Bad Request - {name} should be valid date. Format: YYYY-MM-DD', status_code=400
                    )

        try:
            faqs = self.faq_repo.filter_by(is_deleted=False, **kwargs)
            faqs_list = [faq.to_dict() for faq in faqs.items]

        except DataError:
            enum_values = [value.value for value in FaqCategoryType.__members__.values()]
            return self.handle_response(f'Category should be one of these values {enum_values}', status_code=400)

        return self.handle_response('OK', payload={'faqs': faqs_list, 'meta': self.pagination_meta(faqs)})

    def create_faq(self):

        category, question, answer = self.request_params('category', 'question', 'answer')

        if self.faq_repo.exists(question=question):
            return self.handle_response(f"Question '{question}' already exists", status_code=400)

        faq = self.faq_repo.new_faq(category=category, question=question, answer=answer)
        return self.handle_response('OK', payload={'faq': faq.serialize()}, status_code=201)

    def update_faq(self, faq_id):

        update_info = self.request_params_dict('category', 'question', 'answer')

        faq = self.faq_repo.get(faq_id)

        if faq:
            faq = self.faq_repo.update(faq, **update_info)
            return self.handle_response('OK', payload={'faq': faq.serialize()}, status_code=201)

        return self.handle_response('FAQ Not Found', status_code=404)

    def delete_faq(self, faq_id):
        faq = self.faq_repo.get(faq_id)

        if faq and not faq.is_deleted:
            faq = self.faq_repo.update(faq, **dict(is_deleted=True))
            return self.handle_response('FAQ deleted successfully', payload={'faq': faq.serialize()},
                                        status_code=200)

        return self.handle_response('FAQ Not Found', status_code=404)
