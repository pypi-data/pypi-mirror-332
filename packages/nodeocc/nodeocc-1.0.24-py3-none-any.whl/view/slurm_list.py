from datetime import datetime

from view.styles import _format_to, cmdstyle
from view.utils import is_cvcs_viz, is_student_viz, is_dev, is_prod

midlane = "─────────── ▲ DEV ──────────────────────────────── ▼ PROD ────────────"


def format_date(str_date):
    return datetime.strftime(datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S'), '%m/%d-%H:%M')


def _joblet_format(instance, job, width=74, jobid_type='agg'):
    joblet_reprs = []
    for i, joblet in enumerate(job.joblets):
        jid = str(job.jobid if jobid_type == 'agg' else job.true_jobid)
        joblet_repr = ''
        joblet_repr += _format_to(jid.replace('[', '').replace(']', '').split('%')[0], 14)
        joblet_repr += ' '
        loffset = 0
        if instance.show_prio:
            joblet_repr += '(' + _format_to(job.priority, len(str(job.priority))) + ')'
            joblet_repr += ' '
            loffset += len(str(job.priority)) + 3
        if instance.show_account:
            joblet_repr += _format_to(job.account, 9)
            joblet_repr += ' '
            loffset += 10
        if instance.show_starttime:
            joblet_repr += _format_to(format_date(job.starttime), 12) if not isinstance(job.starttime, float) else _format_to('¯\\_(ツ)_/¯', 11)
            joblet_repr += ' '
            loffset += 13
        joblet_repr += _format_to(job.name if i == 0 else '"', width - 65 - loffset, 'right')
        joblet_repr += ' '
        joblet_repr += _format_to(job.user if i == 0 else '"', 13, 'right')
        joblet_repr += ' '
        joblet_repr += _format_to(job.state if i == 0 else '"', 2, 'right')
        joblet_repr += ' '
        joblet_repr += _format_to(job.runtime if i == 0 else '"', 8, 'right')
        joblet_repr += ' '
        if isinstance(joblet.mem, str):
            mem = '0'
        else:
            mem = round(joblet.mem / 1024)
        joblet_repr += _format_to(f'{mem}G', 4, 'right')
        joblet_repr += ' '
        if instance.view_mode in ('gpu', 'ram'):
            joblet_repr += _format_to((f'{joblet.n_gpus}gp' if joblet.n_gpus > 0 else " - "), 3, 'left')
        elif instance.view_mode == 'cpu':
            joblet_repr += _format_to((f'{joblet.cpus}cp' if joblet.cpus > 0 else " - "), 3, 'left')
        joblet_repr += ' '
        joblet_repr += _format_to(joblet.node if joblet.node is not None else job.reason, 11)
        joblet_reprs.append(joblet_repr)
    job_repr = '\n'.join(joblet_reprs)
    return job_repr


STYLE_MAPPING = {'R': None, 'S': 'MAGENTA', 'PD': 'YELLOW', 'CG': 'MAGENTA'}


def dev_sort_key(x):
    return (x.user,
            x.jobid.split('_')[0],
            int(x.jobid.split('_')[1]) if '_' in x.jobid and '[' not in x.jobid else (999 if '[' in x.jobid else 0))


def prod_sort_key(x, instance):
    return ((x.user if not instance.sort_by_prio else -x.priority,
             x.jobid.split('_')[0],
             int(x.jobid.split('_')[1]) if '_' in x.jobid and '[' not in x.jobid else (999 if '[' in x.jobid else 0)))


def view_list(instance, jobs, filter=None, work=True, stylefn=cmdstyle, current_user=None, width=74, jit='agg'):
    # this is for hot reload
    if not work:
        return "UPDATE IN PROGRESS - PLZ W8 M8 B8"

    # who is the current user?
    if current_user is None:
        import os
        current_user = os.path.basename(os.environ['HOME'])

    # what will this function print?
    printable = set()
    if filter is None:
        printable.add('me')
        printable.add('prod')
        printable.add('stud')
        printable.add('cvcs')
    elif filter == 'me':
        printable.add('me')
    elif filter == 'prod':
        printable.add('prod')
    elif filter == 'stud':
        printable.add('stud')
    elif filter == 'cvcs':
        printable.add('cvcs')

    jobs_to_print = []
    for j in jobs:
        if j.user == current_user and 'me' in printable:
            jobs_to_print.append(j)
        elif 'stud' in printable and is_student_viz(j):
            jobs_to_print.append(j)
        elif 'prod' in printable and not is_student_viz(j):
            jobs_to_print.append(j)
        elif 'cvcs' in printable and is_cvcs_viz(j):
            jobs_to_print.append(j)

    class RetScope:
        return_string = ''

    def cust_print(thing, style=None):
        RetScope.return_string += (thing if style is None else stylefn(style, thing)) + '\n'

    devjobs = sorted([x for x in jobs_to_print if is_dev(x)], key=lambda x: dev_sort_key(x))

    for state in STYLE_MAPPING:
        for x in devjobs:
            if x.state == state:
                cust_print(_joblet_format(instance, x, width=width, jobid_type=jit), style=STYLE_MAPPING[x.state])

    cust_print('─' * ((width - 72) // 2) + midlane + '─' * (width - 72 - ((width - 72) // 2)))

    prodjobs = sorted([x for x in jobs_to_print if not is_dev(x)], key=lambda x: prod_sort_key(x, instance))

    for state in STYLE_MAPPING:
        for x in prodjobs:
            if x.state == state:
                cust_print(_joblet_format(instance, x, width=width, jobid_type=jit), style=STYLE_MAPPING[x.state])

    return RetScope.return_string


if __name__ == '__main__':
    import sys

    from curses_multiwindow import Singleton

    from readers.slurmreader import read_jobs
    instance = Singleton.getInstance()
    jobs, _ = read_jobs()
    if len(sys.argv) > 1 and sys.argv[1] == 'work':
        print(view_list(instance, jobs, work=True, filter='me'))
    elif len(sys.argv) > 1:
        print(view_list(instance, jobs, filter=sys.argv[1]))
    else:
        print(view_list(instance, jobs))
