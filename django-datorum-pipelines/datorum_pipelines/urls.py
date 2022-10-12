from django.contrib import admin
from django.urls import path

from . import views


admin.autodiscover()

app_name = "datorum_pipelines"

urlpatterns = [
    path(
        "list/",
        views.PipelineListView.as_view(),
        name="list",
    ),
    path(
        "<str:slug>/start/",
        views.PipelineStartView.as_view(),
        name="start",
    ),
    path(
        "<str:run_id>/results/",
        views.TaskResultView.as_view(),
        name="results",
    ),
    path(
        "<str:run_id>/results/list/",
        views.TaskResultListView.as_view(),
        name="results-list",
    ),
    path(
        "task-result/<str:pk>/rerun/",
        views.TaskResultReRunView.as_view(),
        name="rerun-task",
    ),
]
