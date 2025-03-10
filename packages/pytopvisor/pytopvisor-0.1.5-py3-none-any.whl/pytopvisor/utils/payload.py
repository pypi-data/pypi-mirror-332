from typing import List, Any, Optional, Dict, Callable
from functools import wraps


def add_universal_params(func: Callable) -> Callable:
    """Decorator to add universal parameters to the payload."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Dict[str, Any]:
        kwargs = {k: v for k, v in kwargs.items() if k != 'self'}
        payload = func(*args, **kwargs)
        universal_params = {
            "limit": int,
            "offset": int,
            "fields": list,
            "filters": List[dict],  # Оставляем как аннотацию, но не для isinstance
            "id": int,
            "orders": list,
        }
        for param, param_type in universal_params.items():
            if param in kwargs and kwargs[param] is not None:
                if param == "filters":
                    # Специальная проверка для filters как списка словарей
                    if not isinstance(kwargs[param], list) or not all(isinstance(f, dict) for f in kwargs[param]):
                        raise ValueError(f"'{param}' must be a list of dictionaries")
                elif not isinstance(kwargs[param], param_type):
                    raise ValueError(f"Param '{param}' must be {param_type.__name__}")
                payload[param] = kwargs[param]
        return payload
    return wrapper

class PayloadFactory:

    @staticmethod
    @add_universal_params
    def projects_get_projects_payload(
        show_site_stat: Optional[bool] = None,
        show_searchers_and_regions: Optional[int] = None,
        include_positions_summary: Optional[bool] = None,
        **kwargs
    ) -> Dict[str, Any] | None:
        """
        Generates payload for the method get/projects_2/projects.
        :param show_site_stat: Add additional project information (boolean).
        :param show_searchers_and_regions: Add a list of search engines and regions (0, 1, 2).
        :param include_positions_summary: Add a summary of positions (boolean).
        :return: Payload for the request.
        """
        payload = {}
        if show_site_stat is not None:
            payload["show_site_stat"] = show_site_stat
        if show_searchers_and_regions is not None:
            payload["show_searchers_and_regions"] = show_searchers_and_regions
        if include_positions_summary is not None:
            payload["include_positions_summary"] = include_positions_summary
        return payload

    @staticmethod
    @add_universal_params
    def projects_get_competitors_payload(
        project_id: int,
        only_enabled: Optional[bool] = None,
        include_project: Optional[bool] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/projects_2/competitors.
        :param project_id: Project ID.
        :param only_enabled: Show only enabled competitors (boolean).
        :param include_project: Include the project itself in the list (boolean).
        :return: Payload for the request.
        """
        payload = {"project_id": project_id}
        if only_enabled is not None:
            payload["only_enabled"] = only_enabled
        if include_project is not None:
            payload["include_project"] = include_project
        return payload

    @staticmethod
    @add_universal_params
    def positions_get_history_payload(
        project_id: int,
        regions_indexes: List[int],
        dates: Optional[List[str]] = None,
        date1: Optional[str] = None,
        date2: Optional[str] = None,
        competitors_ids: Optional[List[int]] = None,
        type_range: Optional[int] = 2,
        count_dates: Optional[int] = None,
        only_exists_first_date: Optional[bool] = None,
        show_headers: Optional[bool] = None,
        show_exists_dates: Optional[bool] = None,
        show_visitors: Optional[bool] = None,
        show_top_by_depth: Optional[int] = None,
        positions_fields: Optional[List[str]] = None,
        filter_by_dynamic: Optional[List[str]] = None,
        filter_by_positions: Optional[List[List[int]]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/positions_2/history.

        :param project_id: Project ID.
        :param regions_indexes: List of region indexes.
        :param dates: List of arbitrary check dates.
        :param date1: Start date of the period.
        :param date2: End date of the period.
        :param competitors_ids: List of competitor IDs (or project ID).
        :param type_range: Date range (enum: 0, 1, 2, 3, 4, 5, 6, 7, 100).
        :param count_dates: Maximum number of returned dates (no more than 31).
        :param only_exists_first_date: Display only keywords present in the first check.
        :param show_headers: Add result headers.
        :param show_exists_dates: Add dates with checks.
        :param show_visitors: Add data about total visits.
        :param show_top_by_depth: Add data for the specified depth of the TOP.
        :param positions_fields: Select columns of data with check results.
        :param filter_by_dynamic: Filter by keywords.
        :param filter_by_positions: Filter by keyword positions.
        :return: Payload for the request.
        """
        # Base payload structure
        payload = {
            "project_id": project_id,
            "regions_indexes": regions_indexes,
            "dates": dates,
            "date1": date1,
            "date2": date2,
            "competitors_ids": competitors_ids,
            "type_range": type_range,
            "count_dates": count_dates,
            "only_exists_first_date": int(only_exists_first_date) if only_exists_first_date is not None else None,
            "show_headers": int(show_headers) if show_headers is not None else None,
            "show_exists_dates": int(show_exists_dates) if show_exists_dates is not None else None,
            "show_visitors": int(show_visitors) if show_visitors is not None else None,
            "show_top_by_depth": show_top_by_depth,
            "positions_fields": positions_fields,
            "filter_by_dynamic": filter_by_dynamic,
            "filter_by_positions": filter_by_positions,
        }
        return {k: v for k, v in payload.items() if v is not None}

    @staticmethod
    @add_universal_params
    def positions_get_summary_payload(
        project_id: int,
        region_index: int,
        dates: List[str],
        competitor_id: Optional[int] = None,
        only_exists_first_date: Optional[bool] = None,
        show_dynamics: Optional[bool] = None,
        show_tops: Optional[bool] = None,
        show_avg: Optional[bool] = None,
        show_visibility: Optional[bool] = None,
        show_median: Optional[bool] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/positions_2/summary.
        :param project_id: Project ID.
        :param region_index: Region index.
        :param dates: List of two dates for building the summary.
        :param competitor_id: Competitor ID (optional).
        :param only_exists_first_date: Consider keywords present in both dates (boolean).
        :param show_dynamics: Add position dynamics (boolean).
        :param show_tops: Add TOP data (boolean).
        :param show_avg: Add average position (boolean).
        :param show_visibility: Add visibility (boolean).
        :param show_median: Add median position (boolean).
        :return: Payload for the request.
        """
        # Base payload structure
        payload = {
            "project_id": project_id,
            "region_index": region_index,
            "dates": dates,
            "competitor_id": competitor_id,
            "only_exists_first_date": int(only_exists_first_date) if only_exists_first_date is not None else None,
            "show_dynamics": int(show_dynamics) if show_dynamics is not None else None,
            "show_tops": int(show_tops) if show_tops is not None else None,
            "show_avg": int(show_avg) if show_avg is not None else None,
            "show_visibility": int(show_visibility) if show_visibility is not None else None,
            "show_median": int(show_median) if show_median is not None else None,
        }
        return {k: v for k, v in payload.items() if v is not None}

    @staticmethod
    @add_universal_params
    def positions_get_summary_chart_payload(
        project_id: int,
        region_index: int,
        dates: Optional[List[str]] = None,
        date1: Optional[str] = None,
        date2: Optional[str] = None,
        competitors_ids: Optional[List[int]] = None,
        type_range: Optional[int] = 2,
        only_exists_first_date: Optional[bool] = None,
        show_tops: Optional[bool] = None,
        show_avg: Optional[bool] = None,
        show_visibility: Optional[bool] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/positions_2/summary/chart.
        :param project_id: Project ID.
        :param region_index: Region index.
        :param dates: List of arbitrary check dates.
        :param date1: Start date of the period.
        :param date2: End date of the period.
        :param competitors_ids: List of competitor IDs (or project ID).
        :param type_range: Date range (enum: 0, 1, 2, 3, 4, 5, 6, 7, 100).
        :param only_exists_first_date: Consider keywords present in all dates (boolean).
        :param show_tops: Add TOP data (boolean).
        :param show_avg: Add average position (boolean).
        :param show_visibility: Add visibility (boolean).
        :return: Payload for the request.
        """
        payload = {
            "project_id": project_id,
            "region_index": region_index,
            "dates": dates,
            "date1": date1,
            "date2": date2,
            "competitors_ids": competitors_ids,
            "type_range": type_range,
            "only_exists_first_date": int(only_exists_first_date) if only_exists_first_date is not None else None,
            "show_tops": int(show_tops) if show_tops is not None else None,
            "show_avg": int(show_avg) if show_avg is not None else None,
            "show_visibility": int(show_visibility) if show_visibility is not None else None,
        }
        return {k: v for k, v in payload.items() if v is not None}


    @staticmethod
    @add_universal_params
    def positions_get_searchers_regions_payload(
        project_id: int,
        searcher_key: Optional[int] = None,
        name_key: Optional[str] = None,
        country_code: Optional[str] = None,
        lang: Optional[str] = None,
        device: Optional[int] = None,
        depth: Optional[int] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/positions_2/searchers/regions/export.
        :param project_id: Project ID.
        :param searcher_key: Search engine key.
        :param name_key: Name or region key.
        :param country_code: Two-letter country code.
        :param lang: Interface language.
        :param device: Device type (enum: 0, 1, 2).
        :param depth: Check depth.
        :return: Payload for the request.
        """
        # Base payload structure
        payload = {
            "project_id": project_id,
            "searcher_key": searcher_key,
            "name/key": name_key,
            "country_code": country_code,
            "lang": lang,
            "device": device,
            "depth": depth,
        }
        return {k: v for k, v in payload.items() if v is not None}


    @staticmethod
    @add_universal_params
    def snapshots_get_history_payload(
        project_id: int,
        region_index: int,
        dates: Optional[List[str]] = None,
        date1: Optional[str] = None,
        date2: Optional[str] = None,
        type_range: Optional[int] = 2,
        count_dates: Optional[int] = None,
        show_exists_dates: Optional[bool] = None,
        show_ams: Optional[bool] = None,
        positions_fields: Optional[List[str]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Generates payload for the method get/positions_2/history.

        :param project_id: Project ID.
        :param region_index: Region index.
        :param dates: List of arbitrary check dates.
        :param date1: Start date of the period.
        :param date2: End date of the period.
        :param type_range: Date range (enum: 0, 1, 2, 3, 4, 5, 6, 7, 100).
        :param count_dates: Maximum number of returned dates (no more than 31).
        :param show_exists_dates: Add dates with checks.
        :param positions_fields: Select columns of data with check results.
        :param show_ams: Add to the result the storm index between the selected checks.
        :return: Payload for the request.
        """
        # Base payload structure
        payload = {
            "project_id": project_id,
            "region_index": region_index,
            "dates": dates,
            "date1": date1,
            "date2": date2,
            "type_range": type_range,
            "count_dates": count_dates,
            "show_exists_dates": int(show_exists_dates) if show_exists_dates is not None else None,
            "show_ams": int(show_ams) if show_ams is not None else None,
            "positions_fields": positions_fields,
        }
        return {k: v for k, v in payload.items() if v is not None}

