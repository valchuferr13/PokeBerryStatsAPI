from django.http import JsonResponse
import json
from django.shortcuts import render
from .pokeapi_data import get_berry_data
import numpy as np
from .berry_growth_histogram import create_histogram


def all_berry_stats(request):
    berry_data = get_berry_data()
    if not berry_data:
        return JsonResponse({'error': 'Unable to retrieve berry data'}, status=500)

    growth_times = list(berry_data.values())

    min_growth_time = min(growth_times)
    median_growth_time = np.median(growth_times)
    max_growth_time = max(growth_times)
    variance_growth_time = np.var(growth_times)
    mean_growth_time = np.mean(growth_times)

    frequency_growth_time = {time: growth_times.count(time) for time in set(growth_times)}

    response_data = {
        "berries_names": list(berry_data.keys()),
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time
    }

    json_data = json.dumps(response_data)
    return render(request, 'stats_api/all_berry_stats.html', {'data': json_data})


def histogram(request):
    berry_data = get_berry_data()
    if not berry_data:
        return render(request, 'error.html', {'message': 'Unable to retrieve berry data'})

    create_histogram(berry_data)
    return render(request, 'stats_api/histogram.html')