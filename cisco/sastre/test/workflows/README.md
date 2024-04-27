# Cisco SASTRE ANSIBLE workflow automation

Cisco Sastre Ansible Test Workflows will automate and test some of the Sastre-Ansible module tasks end to end. 

These workflows will leverage Robot Framework for building and running workflows

## Pre-requisite

Install Robot Framwork : https://pypi.org/project/robotframework/

```
pip install robotframework
```

Run version command to check robot framework is installed successfully

```
% robot --version
Robot Framework 7.0 (Python 3.9.9 on darwin)
```

## NOTES

Please ensure that "test-data" branch has correct data w.r.t SD-WAN version. This data folder will be used throughout the workflows.

## Running the Sastre Ansbile Workflows 

* update and source **env.sh**
```
% source env.sh
```

* Run sastre ansible workflows
```
% sh sastre_ansible_workflow.sh  
```

* Sample output
```
==============================================================================
Sastre Ansible Workflows                                                              
==============================================================================
Workflow_01: Backup_Delete_Restore :: Executing list_config, show_... | PASS |
------------------------------------------------------------------------------
Workflow_02: Detach_Edge_Attach_Edge :: Executing show_template_va... | PASS |
------------------------------------------------------------------------------
Workflow_03: Detach_Vsmart_Attach_Vsmart :: Executing show_templat... | PASS |
------------------------------------------------------------------------------
Sastre Ansible Workflows                                              | PASS |
3 tests, 3 passed, 0 failed
==============================================================================
Output:  < Sastre Ansible Home >/cisco/sastre/test/workflows/output.xml
Log:     < Sastre Ansible Home >/cisco/sastre/test/workflows/log.html
Report:  < Sastre Ansible Home >/cisco/sastre/test/workflows/report.html
```
* Check **report.html** for test report statistics
* Check **log.html** for test logs