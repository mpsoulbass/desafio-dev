from django.db.models import ProtectedError
from rest_framework.exceptions import ValidationError


class ProtectedDestroyMixin:
    protected_model_name = "instance"

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            raise ValidationError(
                {
                    self.protected_model_name: [
                        f"Este(a) {self.protected_model_name} está associado(a) a um(a) ou mais "
                        "registros e não pode ser excluído(a). Para removê-lo(a) é necessário "
                        "deletar todas as suas dependências"
                    ]
                }
            )
