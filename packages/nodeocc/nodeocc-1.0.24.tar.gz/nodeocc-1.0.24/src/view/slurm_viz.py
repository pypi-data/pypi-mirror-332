import random

import pandas as pd
import numpy as np

from view.styles import _format_to, cmdstyle
from view.utils import is_cvcs_viz, is_student_viz, maintenance_status, to_font

ogre = '''⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
    '''
flip = ''' ⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆
 ⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿
 ⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹
 ⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
 ⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
 ⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
 ⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
 ⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟
 ⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃
 ⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠
 ⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾
 ⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿
 ⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿
 ⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿
 ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿
 ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿
 ⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿
 ⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿
 ⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿
 ⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟
    '''
chunga = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    '''

gpu_avail = '□'
gpu_occ = '■'
gpu_drain = '△'
gpu_pendr = '⧖'
gpu_down = '⨯'
gpu_paused = '◆'
gpu_name_chars = 12
gpu_box_chars = 16

mem_size = 16
mem_unit = 'ᴳ'
ram_occ = '█'  # '▄'#
ram_occ_alt = '▀'
ram_avail = '░'
ram_drain = '△'
ram_pendr = '⧖'
ram_paused = '▚'
ram_down = '⨯'

cpu_size = 4
cpu_unit = 'ᶜᵖᵘ'
cpu_occ = '█'  # '▄'#
cpu_occ_alt = '▀'
cpu_avail = '░'
cpu_half = '▌'
cpu_drain = '△'
cpu_pendr = '⧖'
cpu_paused = '▚'
cpu_down = '⨯'

GLOBAL_NODES = None


def get_ram_block(megs):
    return int(round(megs / 1024 / mem_size))


def get_cpu_block(cpus):
    return cpus // cpu_size


def get_node_status(node, jobs):
    ram_occs = 0
    cpu_occs = 0
    for j in sorted(jobs, key=lambda x: (x.partition, x.user)):
        for jj in j.joblets:
            if node.name == jj.node:
                ram_occs += jj.mem
                cpu_occs += jj.cpus

    node_total_ram = node.mem
    node_total_cpus = node.cpus

    # compute the usage percentage for both ram and cpu
    ram_usage = (ram_occs / node_total_ram)
    cpu_usage = (cpu_occs / node_total_cpus)

    # get worst case usage
    usage = max(ram_usage, cpu_usage)

    if usage > 0.9:
        return 'RED'
    elif usage > 0.7:
        return 'YELLOW'
    else:
        return None  # white?


def view_viz(infrastructure, jobs, work=True, stylefn=cmdstyle, current_user=None, mode='gpu'):
    if mode == 'gpu':
        return view_viz_gpu(infrastructure, jobs, work, stylefn, current_user)
    elif mode == 'ram':
        return view_viz_ram(infrastructure, jobs, work, stylefn, current_user)
    elif mode == 'cpu':
        return view_viz_cpu(infrastructure, jobs, work, stylefn, current_user)
    elif mode == 'info':
        return view_viz_info(infrastructure, jobs, work, stylefn, current_user)


def view_viz_ram(infrastructure, jobs, work=True, stylefn=cmdstyle, current_user=None):
    # this is for hot reload
    if not work:
        return "UPDATE IN PROGRESS - PLZ W8 M8 B8"

    # who is the current user?
    if current_user is None:
        import os
        current_user = os.path.basename(os.environ['HOME'])

    nodes = infrastructure.get_sorted_nodes()
    infrast_down = all([x.status == 'down' for x in nodes])

    class RetScope:
        return_string = ''

    def cust_print(thing, style=None):
        RetScope.return_string += (thing if style is None else stylefn(style, thing)) + '\n'

    if not infrast_down:
        highlighted_users = [current_user]
        highlighted_users += pd.DataFrame([(j.user, sum([get_ram_block(x.mem) for x in j.joblets])) for j in jobs if j.user !=
                                          current_user and j.state in ('R', 'S')]).groupby(0).sum()[1].sort_values(ascending=False).iloc[:3].index.to_list()

        user_styles = dict(zip(highlighted_users, ['RED', 'YELLOW', 'GREEN', 'MAGENTA', 'BLUE']))
        students = [j.user for j in jobs if is_student_viz(j)]
        for s in students:
            user_styles[s] = 'CYAN'

        cvcs_students = [j.user for j in jobs if is_cvcs_viz(j)]
        for s in cvcs_students:
            user_styles[s] = 'BLUE'

        stalled_jobs = sum([j.state == 'S' for j in jobs])
        total_jobs_prod = 0
        total_jobs_stud = 0

        # print jobs
        for n in nodes:
            joblet_icons = []
            occs = 0
            for j in sorted(jobs, key=lambda x: (x.partition, x.user)):
                for jj in j.joblets:
                    if n.name == jj.node:
                        if j.is_student() and 'all_usr_prod' in j.partition:
                            total_jobs_stud += int(round((jj.mem) / 1024))
                        elif 'all_usr_prod' in j.partition:
                            total_jobs_prod += int(round((jj.mem) / 1024))
                        occs += jj.mem
                        icon = ram_paused if j.state == 'S' else ram_occ
                        st = icon * get_ram_block(jj.mem)
                        joblet_icons.append((st, user_styles[j.user] if j.user in user_styles else None))
            joblet_icons += [(ram_drain if n.status == 'drain' else (ram_down if n.status == 'down' else (ram_pendr if n.reserved == 'pending' else ram_avail)), None)] * get_ram_block(n.mem - occs)

            jobsplit = [""]
            count = 0
            for ic, c in joblet_icons:
                for i in ic:
                    if count == gpu_box_chars - 3:
                        jobsplit.append("")
                        count = 0
                    bb = ram_occ_alt if len(jobsplit) > 1 and i == ram_occ else i
                    jobsplit[-1] += stylefn(c, bb) if c is not None else bb
                    count += 1
            # if count < gpu_box_chars:
            jobsplit[-1] += f'{to_font(int((n.mem-occs) / 1024))}'

            for i, l in enumerate(jobsplit):
                RetScope.return_string += f'{_format_to(n.name if i == 0 else "", gpu_name_chars, "right")}{"(" if n.reserved == "yes" and i == 0 else " "}{l}{")" if n.reserved == "yes" and i == (len(jobsplit) - 1) else ""}\n'

        # verify maintenance status
        onmain, waitString = maintenance_status(infrastructure)

        # print banner
        if onmain:
            cust_print('  ◀ ONGOING  MAINTENANCE ▶    ', 'BG_MAGENTA')
        elif len(infrastructure.maintenances):
            cust_print('  ◀ MAINTENANCE  in %4s ▶    ' % waitString, 'BG_MAGENTA')
        elif len(jobs) == 0:
            cust_print('         ◀ NO  JOBS ▶         ', 'BG_GREEN')
        elif stalled_jobs / len(jobs) > 0.5:
            cust_print('       ◀ JOBS ON HOLD ▶       ', 'BG_YELLOW')
        else:
            cust_print('')

        cust_print(''.join(['[' + ram_occ + f'{mem_size}{mem_unit}', ram_paused + 'hld', ram_drain + 'drn', ram_pendr + 'pnd', ram_down + 'dwn', '()res]']))
        gpuc = 'GREEN'

        cust_print(' '.join(["  ram:", stylefn(gpuc, (f"{int(round(infrastructure.ram_limit_pu / 1024)):4d}{mem_unit}")
                                               if not pd.isna(infrastructure.ram_limit_pu) else " ∞"),
                             " grp:", stylefn(gpuc, f"{total_jobs_prod:4d}{mem_unit}/{int(round(infrastructure.ram_limit_grp / 1024))}{mem_unit}"
                                              if not pd.isna(infrastructure.ram_limit_grp) else " ∞")]))
        cust_print(' '.join([" Sram:", stylefn('CYAN', (f"{int(round(infrastructure.ram_limit_stu / 1024)):4d}{mem_unit}")
                                               if not pd.isna(infrastructure.ram_limit_stu) else " ∞"),
                             "Sgrp:", stylefn('CYAN', f"{total_jobs_stud:4d}{mem_unit}/{int(round(infrastructure.ram_limit_stugrp / 1024))}{mem_unit}"
                                              if not pd.isna(infrastructure.ram_limit_stugrp) else " ∞")]))

        # print user list
        for u, c in user_styles.items():
            if c in ('CYAN', 'BLUE'):
                continue
            cust_print(
                f" {stylefn(c, gpu_occ)} {stylefn('CYAN', u) if any(['stu' in j.partition for j in jobs if j.user == u]) else u} ({int(round(sum([sum([jj.mem / 1024 for jj in j.joblets if jj.node is not None]) for j in jobs if j.user == u])))}{mem_unit})")
        cust_print(f" {stylefn('CYAN', gpu_occ)} {stylefn('CYAN', 'students')}")
        cust_print(f" {stylefn('BLUE', gpu_occ)} {stylefn('BLUE', 'cvcs/ai4a')}")

    else:  # if infrastrcture_down
        # print emergency screen
        cust_print('  ◀ INFRASTRUCTURE IS DOWN ▶  ', 'BG_RED')
        cust_print(random.choice([flip, chunga, ogre]), 'GREEN')

    return RetScope.return_string


def view_viz_gpu(infrastructure, jobs, work=True, stylefn=cmdstyle, current_user=None):
    # this is for hot reload
    if not work:
        return "UPDATE IN PROGRESS - PLZ W8 M8 B8"

    # who is the current user?
    if current_user is None:
        import os
        current_user = os.path.basename(os.environ['HOME'])

    nodes = infrastructure.get_sorted_nodes()
    infrast_down = all([x.status == 'down' for x in nodes])

    class RetScope:
        return_string = ''

    def cust_print(thing, style=None):
        RetScope.return_string += (thing if style is None else stylefn(style, thing)) + '\n'

    if not infrast_down:
        highlighted_users = [current_user]
        highlighted_users += pd.DataFrame([(j.user, sum([x.n_gpus for x in j.joblets])) for j in jobs if j.user != current_user and j.state in ('R', 'S')]
                                          ).groupby(0).sum()[1].sort_values(ascending=False).iloc[:3].index.to_list()

        user_styles = dict(zip(highlighted_users, ['RED', 'YELLOW', 'GREEN', 'MAGENTA', 'BLUE']))
        students = [j.user for j in jobs if is_student_viz(j)]
        for s in students:
            user_styles[s] = 'CYAN'

        cvcs_students = [j.user for j in jobs if is_cvcs_viz(j)]
        for s in cvcs_students:
            user_styles[s] = 'BLUE'

        stalled_jobs = sum([j.state == 'S' for j in jobs])
        total_jobs_prod = 0
        total_jobs_stud = 0

        # print jobs
        for n in nodes:
            joblet_icons = []
            occs = 0
            for j in jobs:
                for jj in j.joblets:
                    if jj.n_gpus == 0:
                        continue
                    if n.name == jj.node:
                        if j.is_student() and 'all_usr_prod' in j.partition:
                            total_jobs_stud += jj.n_gpus
                        elif 'all_usr_prod' in j.partition:
                            total_jobs_prod += jj.n_gpus
                        occs += jj.n_gpus
                        icon = gpu_paused if j.state == 'S' else gpu_occ
                        st = icon + (('+' if len(j.joblets) > 1 else '-') + icon) * (jj.n_gpus - 1)
                        joblet_icons.append((st, user_styles[j.user] if j.user in user_styles else None))
            joblet_icons += [(gpu_drain if n.status == 'drain' else (gpu_down if n.status == 'down' else (gpu_pendr if n.reserved == 'pending' else gpu_avail)), None)] * (n.n_gpus - occs)

            joblet_icons = [(ji[0] + (' ' if i != len(joblet_icons) - 1 else ''), ji[1]) for i, ji in enumerate(joblet_icons)]

            node_status = get_node_status(n, jobs)
            jobsplit = [""]
            count = 0
            for ic, c in joblet_icons:
                for i in ic:
                    if count == gpu_box_chars:
                        jobsplit.append("")
                        count = 0
                    if c is not None:
                        jobsplit[-1] += stylefn(c, i)
                    elif node_status is not None and i != gpu_occ:
                        jobsplit[-1] += stylefn(node_status, i)
                    else:
                        jobsplit[-1] += i
                    count += 1

            for i, l in enumerate(jobsplit):
                RetScope.return_string += f'{_format_to(n.name if i == 0 else "", gpu_name_chars, "right")}{"(" if n.reserved == "yes" and i == 0 else " "}{l}{")" if n.reserved == "yes" and i == (len(jobsplit) - 1) else ""}\n'

        # verify maintenance status
        onmain, waitString = maintenance_status(infrastructure)

        # print banner
        if onmain:
            cust_print('  ◀ ONGOING  MAINTENANCE ▶    ', 'BG_MAGENTA')
        elif len(infrastructure.maintenances):
            cust_print('  ◀ MAINTENANCE  in %4s ▶    ' % waitString, 'BG_MAGENTA')
        elif len(jobs) == 0:
            cust_print('         ◀ NO  JOBS ▶         ', 'BG_GREEN')
        elif stalled_jobs / len(jobs) > 0.5:
            cust_print('       ◀ JOBS ON HOLD ▶       ', 'BG_YELLOW')
        else:
            cust_print('')

        # print summary
        cust_print(''.join([' [' + gpu_occ + 'run ()resv ', stylefn('YELLOW', gpu_avail) + '>70% ', stylefn('RED', gpu_avail), '>90%]']))
        cust_print(''.join([' [', gpu_paused + 'hld ', gpu_drain + 'drn ', gpu_pendr + 'pnd ', gpu_down + 'dwn', ']']))
        gpuc = 'RED'
        if infrastructure.gpu_limit_pu > 3:
            gpuc = 'YELLOW'
        if infrastructure.gpu_limit_pu > 6:
            gpuc = 'GREEN'
        cust_print(' '.join(["      gpu:", stylefn(gpuc, ("%2d" % infrastructure.gpu_limit_pu) if not pd.isna(infrastructure.gpu_limit_pu) else " ∞"), " grp:",
                   stylefn(gpuc, "%2d/%s") % (total_jobs_prod, ("%2d" % infrastructure.gpu_limit_grp) if not pd.isna(infrastructure.gpu_limit_grp) else " ∞")]))
        cust_print(' '.join(["     Sgpu:", stylefn('CYAN', ("%2d" % infrastructure.gpu_limit_stu) if not pd.isna(infrastructure.gpu_limit_stu) else " ∞"), "Sgrp:",
                   stylefn('CYAN', "%2d/%s") % (total_jobs_stud, ("%2d" % infrastructure.gpu_limit_stugrp) if not pd.isna(infrastructure.gpu_limit_stugrp) else " ∞")]))

        # print user list
        for u, c in user_styles.items():
            if c in ('CYAN', 'BLUE'):
                continue
            cust_print(
                f" {stylefn(c, gpu_occ)} {stylefn('CYAN', u) if any(['stu' in j.partition for j in jobs if j.user == u]) else u} ({sum([sum([jj.n_gpus for jj in j.joblets if jj.node is not None]) for j in jobs if j.user == u])})")
        cust_print(f" {stylefn('CYAN', gpu_occ)} {stylefn('CYAN', 'students')} ({sum([sum([jj.n_gpus for jj in j.joblets if jj.node is not None]) for j in jobs if is_student_viz(j)])})")
        cust_print(f" {stylefn('BLUE', gpu_occ)} {stylefn('BLUE', 'cvcs/ai4a')} ({sum([sum([jj.n_gpus for jj in j.joblets if jj.node is not None]) for j in jobs if is_cvcs_viz(j)])})")

    else:  # if infrastrcture_down
        # print emergency screen
        cust_print('  ◀ INFRASTRUCTURE IS DOWN ▶  ', 'BG_RED')
        cust_print(random.choice([flip, chunga, ogre]), 'GREEN')

    return RetScope.return_string


def get_cpu_icon(stat):
    return {
        'drain': cpu_drain,
        'down': cpu_down,
        'pending': cpu_pendr,
    }.get(stat, cpu_avail)


def view_viz_cpu(infrastructure, jobs, work=True, stylefn=cmdstyle, current_user=None):
    # this is for hot reload
    if not work:
        return "UPDATE IN PROGRESS - PLZ W8 M8 B8"

    # who is the current user?
    if current_user is None:
        import os
        current_user = os.path.basename(os.environ['HOME'])

    nodes = infrastructure.get_sorted_nodes()
    infrast_down = all([x.status == 'down' for x in nodes])

    class RetScope:
        return_string = ''

    def cust_print(thing, style=None):
        RetScope.return_string += (thing if style is None else stylefn(style, thing)) + '\n'

    if not infrast_down:
        highlighted_users = [current_user]
        highlighted_users += pd.DataFrame([(j.user, sum([x.cpus for x in j.joblets])) for j in jobs if j.user != current_user and j.state in ('R', 'S')]
                                          ).groupby(0).sum()[1].sort_values(ascending=False).iloc[:3].index.to_list()

        user_styles = dict(zip(highlighted_users, ['RED', 'YELLOW', 'GREEN', 'MAGENTA', 'BLUE']))
        students = [j.user for j in jobs if is_student_viz(j)]
        for s in students:
            user_styles[s] = 'CYAN'

        cvcs_students = [j.user for j in jobs if is_cvcs_viz(j)]
        for s in cvcs_students:
            user_styles[s] = 'BLUE'

        stalled_jobs = sum([j.state == 'S' for j in jobs])
        total_jobs_prod = 0
        total_jobs_stud = 0

        # print jobs
        for n in nodes:
            joblet_icons = []
            occs = 0
            none_st = 0
            for j in sorted(jobs, key=lambda x: (x.partition, x.user)):
                for jj in j.joblets:
                    if n.name == jj.node:
                        if j.is_student() and 'all_usr_prod' in j.partition:
                            total_jobs_stud += jj.cpus
                        elif 'all_usr_prod' in j.partition:
                            total_jobs_prod += jj.cpus
                        occs += jj.cpus
                        icon = cpu_paused if j.state == 'S' else cpu_occ
                        st = icon * get_cpu_block(jj.cpus)
                        if st == '':
                            none_st += jj.cpus
                        joblet_icons.append((st, user_styles[j.user] if j.user in user_styles else None))
            if none_st > 0:
                joblet_icons += [(cpu_occ, None)] * get_cpu_block(none_st)
                if none_st % cpu_size != 0:
                    joblet_icons.append((cpu_occ_alt, None))
            joblet_icons += [(get_cpu_icon(n.status), None)] * get_cpu_block(n.cpus - occs)

            jobsplit = [""]
            count = 0
            for ic, c in joblet_icons:
                for i in ic:
                    if count == gpu_box_chars - 3:
                        jobsplit.append("")
                        count = 0
                    bb = cpu_occ_alt if len(jobsplit) > 1 and i == cpu_occ else i
                    jobsplit[-1] += stylefn(c, bb) if c is not None else bb
                    count += 1
            # if count < gpu_box_chars:
            jobsplit[-1] += f'{to_font(n.cpus-occs)}/{to_font(n.cpus)}'

            for i, l in enumerate(jobsplit):
                RetScope.return_string += f'{_format_to(n.name if i == 0 else "", gpu_name_chars, "right")}{"(" if n.reserved == "yes" and i == 0 else " "}{l}{")" if n.reserved == "yes" and i == (len(jobsplit) - 1) else ""}\n'

        # verify maintenance status
        onmain, waitString = maintenance_status(infrastructure)

        # print banner
        if onmain:
            cust_print('  ◀ ONGOING  MAINTENANCE ▶    ', 'BG_MAGENTA')
        elif len(infrastructure.maintenances):
            cust_print('  ◀ MAINTENANCE  in %4s ▶    ' % waitString, 'BG_MAGENTA')
        elif len(jobs) == 0:
            cust_print('         ◀ NO  JOBS ▶         ', 'BG_GREEN')
        elif stalled_jobs / len(jobs) > 0.5:
            cust_print('       ◀ JOBS ON HOLD ▶       ', 'BG_YELLOW')
        else:
            cust_print('')

        # print summary
        # cust_print(''.join([' ['+ ram_occ + 'run', paused + 'hld', drain + 'drn', down + 'dwn', '()res]']))
        cust_print(''.join(['[' + ram_occ + f'{cpu_size}{cpu_unit}', cpu_paused + 'hld', cpu_drain + 'drn', cpu_pendr + 'pnd', cpu_down + 'dwn', '()res]']))
        gpuc = 'GREEN'
        # if infrastructure.gpu_limit_pu > 3:
        #     gpuc = 'YELLOW'
        # if infrastructure.gpu_limit_pu > 6:
        #     gpuc = 'GREEN'
        cust_print(' '.join(["  cpu:", stylefn(gpuc, (f"{int(round(infrastructure.cpu_limit_pu)):4d}{cpu_size}")
                                               if not pd.isna(infrastructure.cpu_limit_pu) else " ∞"),
                             " grp:", stylefn(gpuc, f"{total_jobs_prod:4d}{cpu_size}/{int(round(infrastructure.cpu_limit_grp))}{cpu_size}"
                                              if not pd.isna(infrastructure.cpu_limit_grp) else " ∞ ")]))
        cust_print(' '.join([" Scpu:", stylefn('CYAN', (f"{int(round(infrastructure.cpu_limit_stu)):4d}{cpu_size}")
                                               if not pd.isna(infrastructure.cpu_limit_stu) else " ∞"),
                             "Sgrp:", stylefn('CYAN', f"{total_jobs_stud:4d}{cpu_size}/{int(round(infrastructure.cpu_limit_stugrp))}{cpu_size}"
                                              if not pd.isna(infrastructure.cpu_limit_stugrp) else " ∞ ")]))

        # print user list
        for u, c in user_styles.items():
            if c in ('CYAN', 'BLUE'):
                continue
            cust_print(
                f" {stylefn(c, gpu_occ)} {stylefn('CYAN', u) if any(['stu' in j.partition for j in jobs if j.user == u]) else u} ({sum([sum([jj.cpus for jj in j.joblets if jj.node is not None]) for j in jobs if j.user == u])}{cpu_unit})")
        cust_print(f" {stylefn('CYAN', gpu_occ)} {stylefn('CYAN', 'students')}")
        cust_print(f" {stylefn('BLUE', gpu_occ)} {stylefn('BLUE', 'cvcs/ai4a')}")

    else:  # if infrastrcture_down
        # print emergency screen
        cust_print('  ◀ INFRASTRUCTURE IS DOWN ▶  ', 'BG_RED')
        cust_print(random.choice([flip, chunga, ogre]), 'GREEN')

    return RetScope.return_string


def view_viz_info(infrastructure, jobs, work=True, stylefn=cmdstyle, current_user=None):
    # this is for hot reload
    if not work:
        return "UPDATE IN PROGRESS - PLZ W8 M8 B8"

    global GLOBAL_NODES
    if GLOBAL_NODES is None:
        from readers.slurmreader import _read_nodes, _node_preproc
        GLOBAL_NODES = _read_nodes(return_raw=True)
        GLOBAL_NODES.loc[:, 'nodename'] = GLOBAL_NODES.NODELIST.apply(_node_preproc)
        prior = ['n/a', None, 'A40', 'RTXA5000', 'RTX6000', 'RTX5000', '2080', 'V100', '1080', 'P100', 'K80']
        reord_idx = sorted(zip(GLOBAL_NODES['m_gpu'], GLOBAL_NODES.index), key=lambda g: prior.index(g[0].split(',')[0]) if g[0].split(',')[0] in prior else -1)
        GLOBAL_NODES = GLOBAL_NODES.loc[np.array([i for x, i in reord_idx])].reset_index(drop=True)

    # who is the current user?
    if current_user is None:
        import os
        current_user = os.path.basename(os.environ['HOME'])

    # nodes = infrastructure.get_sorted_nodes()
    infrast_down = all([x.status == 'down' for x in infrastructure.get_sorted_nodes()])

    class RetScope:
        return_string = ''

    def cust_print(thing, style=None):
        RetScope.return_string += (thing if style is None else stylefn(style, thing)) + '\n'

    if not infrast_down:
        stalled_jobs = sum([j.state == 'S' for j in jobs])
        # max_gpu_len = max([len(n.gpu_model) + len(str(n.n_gpus)) if n.gpu_model is not None else 0 for n in nodes])
        # max_n_gpu_len = max([len(str(n.n_gpus)) for n in nodes])
        # max_cpu_len = max([len(str(n.cpus)) for n in nodes] + [len('CPUs')])
        # max_ram_len = max([len(str(n.mem // 1024)) for n in nodes])
        feat_str = stylefn("GREEN", "FEATURES")
        RetScope.return_string += f'{"":{gpu_name_chars}} GPU {feat_str}\n'
        for i, n in GLOBAL_NODES.iterrows():
            gpu_model = n.m_gpu  # if n.m_gpu is not None else 'N/A'
            # gpu_mem = n.gpu_mem if n.gpu_mem is not None else 'N/A'
            mem = n.MEMORY // 1024 if n.MEMORY is not None else 'N/A'
            n_gpus = n.n_gpu if n.n_gpu is not None else 'N/A'
            n_cpus = n.CPUS  # if n.CPUS is not None else 'N/A'
            # gpu_mem = GPU_MEM.get(gpu_model, 'N/A')

            gpu_feature = n.AVAIL_FEATURES  # if n.feature is not None else '(null)'

            # gpu_mem = ','.join([str(GPU_MEM.get(x, 'N/A')) for x in gpu_model.split(',')])
            # gpu_str = f'{n_gpus}x{gpu_model:{max_gpu_len-(1*(len(str(n_gpus))))}}' if n_gpus != 0 else f'{"N/A":{max_gpu_len+1}}'
            if n_gpus != 0:
                gpu_str = f'{stylefn("RED", str(n_gpus))}'
                if gpu_feature != '(null)':
                    gpu_str += f'x{stylefn("GREEN", gpu_feature)}'
                else:
                    gpu_str += f'@({stylefn("YELLOW", gpu_model)})'
            else:
                gpu_str = "N/A"  # f'{"N/A":{max_gpu_len+1}}'

            RetScope.return_string += f'{_format_to(n.nodename, gpu_name_chars, "right")} {gpu_str}\n'
            # RetScope.return_string += f'{"":{gpu_name_chars}} {"VRAM":{max_gpu_len+1}} {f"{mem}G"}\n'

    onmain, waitString = maintenance_status(infrastructure)
    if onmain:
        cust_print('  ◀ ONGOING  MAINTENANCE ▶    ', 'BG_MAGENTA')
    elif len(infrastructure.maintenances):
        cust_print('  ◀ MAINTENANCE  in %4s ▶    ' % waitString, 'BG_MAGENTA')
    elif len(jobs) == 0:
        cust_print('         ◀ NO  JOBS ▶         ', 'BG_GREEN')
    elif stalled_jobs / len(jobs) > 0.5:
        cust_print('       ◀ JOBS ON HOLD ▶       ', 'BG_YELLOW')
    else:
        cust_print('')

    # print summary
    # cust_print(''.join([' ['+ ram_occ + 'run', paused + 'hld', drain + 'drn', down + 'dwn', '()res]']))
    # cust_print(''.join(['[' + ram_occ + f'{cpu_size}{cpu_unit}', cpu_paused + 'hld', cpu_drain + 'drn', cpu_pendr + 'pnd', cpu_down + 'dwn', '()res]']))
    # gpuc = 'GREEN'

    return RetScope.return_string


if __name__ == '__main__':
    import sys

    from readers.slurmreader import read_infrastructure, read_jobs
    infr = read_infrastructure()
    jobs, _ = read_jobs()
    if len(sys.argv) > 1 and sys.argv[1] == 'work':
        print(view_viz_gpu(infr, jobs, work=True))
        print(view_viz_ram(infr, jobs, work=True))
    else:
        print(view_viz_gpu(infr, jobs))
        print(view_viz_ram(infr, jobs))
