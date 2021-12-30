from rest_framework.routers import (
    SimpleRouter,
    Route,
    escape_curly_brackets,
)


class StaticRouter(SimpleRouter):
    """Router that doesn't generated dynamicly default routes for create/list/retrieve/... actions.

    That means you have to use `@action` decorator on all actions you want to create,
    included "list", "create", "retrieve", "update", "partial_update" and "destroy".

    Notes
    -----
    For "default" actions (create, list, ...), you could avoid `url_path` parameters.

    """

    routes = []

    def get_routes(self, viewset):
        routes = [
            self._get_route_from_action(action)
            for action in viewset.get_extra_actions()
        ]
        return routes

    def _get_route_from_action(self, action):
        return Route(
            url=self._get_url(action.detail, action.url_path).replace(
                "{url_path}", escape_curly_brackets(action.url_path)
            ),
            mapping=action.mapping,
            name="{basename}-{url_name}".replace("{url_name}", action.url_name),
            detail=action.detail,
            initkwargs=action.kwargs.copy(),
        )

    def _get_url(self, detail: bool, url_path: str):
        indexes_actions = [
            "list",
            "create",
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ]

        if not detail and url_path in indexes_actions:
            return r"^{prefix}{trailing_slash}$"
        elif not detail:
            return r"^{prefix}/{url_path}{trailing_slash}$"
        elif detail and url_path in indexes_actions:
            return r"^{prefix}/{lookup}{trailing_slash}$"
        elif detail:
            return r"^{prefix}/{lookup}/{url_path}{trailing_slash}$"
        else:
            raise Exception(
                f"Not url found for detail#{detail} and url_path#{url_path}"
            )
