from ansible.module_utils.basic import env_fallback
from cisco_sdwan.tasks.common import TaskException
from cisco_sdwan.base.rest_api import Rest
from cisco_sdwan.cmd import VMANAGE_PORT, REST_TIMEOUT, BASE_URL


def common_arg_spec():
    return dict(
        address=dict(type="str", fallback=(env_fallback, ['VMANAGE_IP'])),
        user=dict(type="str", fallback=(env_fallback, ['VMANAGE_USER'])),
        password=dict(type="str", no_log=True, fallback=(env_fallback, ['VMANAGE_PASSWORD'])),
        tenant=dict(type="str"),
        pid=dict(type="str", default="0", fallback=(env_fallback, ['CX_PID'])),
        port=dict(type="int", default=VMANAGE_PORT, fallback=(env_fallback, ['VMANAGE_PORT'])),
        timeout=dict(type="int", default=REST_TIMEOUT),
    )
    
def module_params(*param_names, module_param_dict):
    return {
       name: module_param_dict.get(name) for name in param_names if module_param_dict.get(name) is not None
    }


def sdwan_api_args(module_param_dict):
    missing_required = [
        required_param for required_param in ['address', 'user', 'password']
        if not module_param_dict[required_param]
    ]
    if missing_required:
        raise TaskException(f"Missing parameters: {', '.join(missing_required)}")

    api_args = {
        'base_url': BASE_URL.format(address=module_param_dict['address'], port=module_param_dict['port']),
        'username': module_param_dict['user'],
        'password': module_param_dict['password'],
        'timeout': module_param_dict['timeout']
    }
    if module_param_dict['tenant'] is not None:
        api_args['tenant'] = module_param_dict['tenant']

    return api_args


def run_task(task_cls, task_args, module_param_dict):
    task = task_cls()
    task_output = execute_task(task, task_args, module_param_dict)

    result = {}
    if task_output:
        result["stdout"] = "\n\n".join(str(entry) for entry in task_output)

    result["msg"] = f"Task completed {task.outcome('successfully', 'with caveats: {tally}')}"

    return result

def execute_task(task, task_args, module_param_dict):
    if task.is_api_required(task_args):
        with Rest(**sdwan_api_args(module_param_dict=module_param_dict)) as api:
            task_output = task.runner(task_args, api)
    else:
        task_output = task.runner(task_args)
    
    return task_output

def is_mutually_exclusive(mutual_exclusive_fields, **kwargs):
    if mutual_exclusive_fields is not None and len(mutual_exclusive_fields) > 1:
        is_mutually_exlusive: bool = False
        for arg in mutual_exclusive_fields:
            if kwargs.get(arg) is None:
                continue
            elif is_mutually_exlusive:
                return is_mutually_exlusive
            is_mutually_exlusive = True
          