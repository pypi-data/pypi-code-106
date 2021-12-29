# coding=utf-8
"""Process comfort map results into thermal comfort percent."""
from __future__ import division
import json


def tcp_model_schedules(condition_csv, enclosure_info_json, occ_schedule_json):
    """Compute Thermal Comfort Petcent (TCP) using model-exported occupancy schedules.

    Args:
        condition_csv: Path to a CSV file of thermal conditions output by a
            thermal mapping command.
        enclosure_info_json: Path to a JSON file containing information about
            the radiant enclosure that sensor points belong to. Note that this
            enclosure JSON should be for the same grid as the condition_csv.
        occ_schedule_json: Path to an occupancy schedule JSON output by the
            honeybee-energy model-occ-schedules command.

    Returns:
        A tuple fo three values

        * tcp_list -- List of Thermal Comfort Percent (TCP) values for each sensor.

        * hsp_list -- List of Heat Sensation Percent (HSP) values for each sensor.

        * csp_list - List of Cold Sensation Percent (CSP) values for each sensor.
    """
    # parse all of the input files
    with open(enclosure_info_json) as json_file:
        enclosure_dict = json.load(json_file)
    cond_mtx = []
    with open(condition_csv) as csv_data_file:
        for row in csv_data_file:
            cond_mtx.append([int(val) for val in row.split(',')])
    with open(occ_schedule_json) as json_file:
        occ_dict = json.load(json_file)

    # order the occ schedule data based on the relevant zones from the enclosure_info
    occ_values, total_occs, time_count = [], [], len(cond_mtx[0])
    for zone_id in enclosure_dict['mapper']:
        sch_id = occ_dict['room_occupancy'][zone_id]
        if sch_id is not None:
            sch_vals = occ_dict['schedules'][sch_id]
            occ_values.append(sch_vals)
            total_occs.append(sum(sch_vals))
        else:
            occ_values.append(None)
            total_occs.append(None)
    if enclosure_dict['has_outdoor']:
        sch_vals = [1] * time_count  # assume the outdoors is always occupied
        occ_values.append(sch_vals)
        total_occs.append(time_count)

    # loop through the sensors and compute tcp, hsp, and csp
    tcp_list, hsp_list, csp_list = [], [], []
    for pt_i, conditions in zip(enclosure_dict['sensor_indices'], cond_mtx):
        occ_sch, total_occ = occ_values[pt_i], total_occs[pt_i]
        if occ_sch is not None and total_occ != 0:
            tcp, hsp, csp = 0, 0, 0
            for occ, cond in zip(occ_sch, conditions):
                if occ == 1:
                    if cond == 0:
                        tcp += 1
                    elif cond == 1:
                        hsp += 1
                    else:
                        csp += 1
            tcp_list.append((tcp / total_occ) * 100)
            hsp_list.append((hsp / total_occ) * 100)
            csp_list.append((csp / total_occ) * 100)
        else:  # the space is unoccupied; treat it as all comfortable
            tcp_list.append(100)
            hsp_list.append(0)
            csp_list.append(0)
    return tcp_list, hsp_list, csp_list


def tcp_total(condition_csv):
    """Compute Thermal Comfort Petcent (TCP) assuming all times are occupied.

    Args:
        condition_csv: Path to a CSV file of thermal conditions output by a
            thermal mapping command.

    Returns:
        A tuple fo three values.

        * tcp_list -- List of Thermal Comfort Percent (TCP) values for each sensor.

        * hsp_list -- List of Heat Sensation Percent (HSP) values for each sensor.

        * csp_list - List of Cold Sensation Percent (CSP) values for each sensor.
    """
    # parse the csv of results
    cond_mtx = []
    with open(condition_csv) as csv_data_file:
        for row in csv_data_file:
            cond_mtx.append([int(val) for val in row.split(',')])

    # loop through the sensors and compute tcp, hsp, and csp
    tcp_list, hsp_list, csp_list, total_occ = [], [], [], len(cond_mtx[0])
    for conditions in cond_mtx:
        tcp, hsp, csp = 0, 0, 0
        for cond in conditions:
            if cond == 0:
                tcp += 1
            elif cond == 1:
                hsp += 1
            else:
                csp += 1
        tcp_list.append((tcp / total_occ) * 100)
        hsp_list.append((hsp / total_occ) * 100)
        csp_list.append((csp / total_occ) * 100)
    return tcp_list, hsp_list, csp_list
