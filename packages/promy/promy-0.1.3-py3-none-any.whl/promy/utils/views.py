from django.utils.timezone import now
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

__all__ = ["BaseModelViewSet", "UserIdViewMixin"]


class BaseModelViewSet(ModelViewSet):
    request_serializer = None
    response_serializer = None

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return self.request_serializer or self.serializer_class

        return self.response_serializer or self.serializer_class

    def destroy(self, request: Request, *args, **kwargs):
        instance = self.get_object()

        if hasattr(instance, "archived_at"):
            instance.archived_at = now()
            instance.save()
        else:
            self.perform_destroy(instance)

        return Response(status=status.HTTP_200_OK)


class UserIdViewMixin:
    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.kwargs.get("user_id"))

    def get_serializer_context(self):
        return {
            **super().get_serializer_context(),
            "user_id": self.kwargs.get("user_id"),
        }
