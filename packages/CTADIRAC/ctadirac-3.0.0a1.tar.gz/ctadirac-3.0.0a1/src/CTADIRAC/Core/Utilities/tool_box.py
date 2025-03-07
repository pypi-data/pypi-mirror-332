""" Helper module that contains a set of useful simple and generic functions

                    JB, September 2018
"""

__RCSID__ = "$Id$"

import copy
import datetime
import os
import re

import DIRAC
from DIRAC.Core.Utilities.ReturnValues import returnSingleResult
from DIRAC.Resources.Catalog.FileCatalogClient import FileCatalogClient

# Jobs status dictionnary
BASE_STATUS_DIR = {
    "Received": 0,
    "Matched": 0,
    "Waiting": 0,
    "Running": 0,
    "Failed": 0,
    "Stalled": 0,
    "Rescheduled": 0,
    "Checking": 0,
    "Done": 0,
    "Completing": 0,
    "Completed": 0,
    "Killed": 0,
    "Total": 0,
}

# Data level meta data id
DATA_LEVEL_METADATA_ID = {
    "MC0": -3,
    "R0": -2,
    "R1": -1,
    "DL0": 0,
    "DL1": 1,
    "DL2": 2,
    "DL3": 3,
    "DL4": 4,
    "DL5": 5,
}


def highlight(string):
    """highlight a string in a terminal display"""
    return f"\x1b[31;1m{string}\x1b[0m"


def read_inputs_from_file(file_path):
    """Read inputs from an ASCII files
    Used for list of LFN or list of datasets
    Expects just one LFN/dataset per line
    """
    content = open(file_path).readlines()
    input_file_list = []
    for line in content:
        infile = line.strip()
        if line != "\n":
            input_file_list.append(infile)
    return input_file_list


def run_number_from_filename(filename, package):
    """try to get a run number from the file name

    return:
        run_number : int - the run number
    """
    run_number = -1
    if filename[-9:] == ".logs.tgz":
        run_number = int(filename.split("/")[-1].split("_")[-1].split(".")[0])
    elif package in ["chimp", "mars"]:
        run_number = int(filename.split("run")[1].split("___cta")[0])
    elif package in ["corsika_simhessarray", "corsika_simtelarray"]:
        if filename[-12:] in [".corsika.zst"]:
            # int(re.findall(r'run\d+_', os.path.basename(filename))[0].strip('run_'))
            run_number = int(os.path.basename(filename).split("_")[0].strip("run"))
        elif filename.find("tid") > 0:
            run_number = int(
                re.findall(r"tid\d+", os.path.basename(filename))[0].strip("tid")
            )
        elif os.path.splitext(filename)[1] in [".log"]:
            run_number = int(os.path.basename(filename).strip("run.log"))
        else:
            run_number = int(filename.split("run")[1].split("___cta")[0])
    elif "evndisplay" in package:
        if filename.find("tid") > 0:
            run_number = int(
                re.findall(r"tid\d+", os.path.basename(filename))[0].strip("tid")
            )
        elif filename[-8:] in ["DL1.root", "DL2.root"]:
            run_number = int(filename.split("run")[1].split("___cta")[0])
        elif filename[-10:] in ["DL1.tar.gz", "DL2.tar.gz"]:
            run_number = int(filename.split("run")[1].split("___cta")[0])
        else:
            run_number = int(filename.split("-")[0])  # old default
    elif package == "image_extractor":
        run_number = int(filename.split("srun")[1].split("-")[0])
    elif package == "dl1_data_handler":
        run_number = int(filename.split("runs")[1].split("-")[0])
    elif "ctapipe" in package:
        run_number = int(filename.split("run")[1].split("___cta")[0])
    return run_number


def check_dataset_query(dataset_name):
    """print dfind command for a given dataset"""
    md_dict = get_dataset_MQ(dataset_name)
    return debug_query(md_dict)


def debug_query(MDdict):
    """just unwrap a meta data dictionnary into a dfind command"""
    msg = "dfind /vo.cta.in2p3.fr/MC/"
    for key, val in MDdict.items():
        try:
            val = val.values()[0]
        except BaseException:
            pass
        msg += f" {key}={val}"
    return msg


def get_dataset_MQ(dataset_name):
    """Return the Meta Query associated with a given dataset"""
    fc = FileCatalogClient()
    result = returnSingleResult(fc.getDatasetParameters(dataset_name))
    if not result["OK"]:
        DIRAC.gLogger.error("Failed to retrieved dataset:", result["Message"])
        DIRAC.exit(-1)
    else:
        DIRAC.gLogger.info("Successfully retrieved dataset: ", dataset_name)
    return result["Value"]["MetaQuery"]


def get_job_list(owner, job_group, n_hours):
    """get a list of jobs for a selection"""
    from DIRAC.Interfaces.API.Dirac import Dirac

    dirac = Dirac()

    now = datetime.datetime.now()
    onehour = datetime.timedelta(hours=1)
    results = dirac.selectJobs(
        jobGroup=job_group, owner=owner, date=now - n_hours * onehour
    )
    if "Value" not in results:
        DIRAC.gLogger.error(
            'No job found for group "%s" and owner "%s" in the past %s hours'
            % (job_group, owner, n_hours)
        )
        DIRAC.exit(-1)

    # Found some jobs, print information)
    jobs_list = results["Value"]
    return jobs_list


def parse_jobs_list(jobs_list):
    """parse a jobs list by first getting the status of all jobs"""
    from DIRAC.Interfaces.API.Dirac import Dirac

    dirac = Dirac()
    # status of all jobs
    status = dirac.getJobStatus(jobs_list)
    # parse it
    sites_dict = {}
    status_dict = copy.copy(BASE_STATUS_DIR)
    for job in jobs_list:
        site = status["Value"][int(job)]["Site"]
        majstatus = status["Value"][int(job)]["Status"]
        if majstatus not in status_dict.keys():
            DIRAC.gLogger.notice(f"Add {majstatus} to BASE_STATUS_DIR")
            DIRAC.sys.exit(1)
        status_dict[majstatus] += 1
        status_dict["Total"] += 1
        if site not in sites_dict.keys():
            if site.find(".") == -1:
                site = "    None"  # note that blank spaces are needed
            sites_dict[site] = copy.copy(BASE_STATUS_DIR)
            sites_dict[site][majstatus] = 1
            sites_dict[site]["Total"] = 1
        else:
            sites_dict[site]["Total"] += 1
            if majstatus not in sites_dict[site].keys():
                sites_dict[site][majstatus] = 1
            else:
                sites_dict[site][majstatus] += 1
    return status_dict, sites_dict


def get_os_and_cpu_info():
    """get OS and instructions supported by current cpu"""
    import platform
    import re
    import subprocess

    platform = platform.platform()
    cpuinfo = subprocess.check_output("cat /proc/cpuinfo", shell=True, text=True)
    model_name = subprocess.check_output(
        'grep -m 1 "model name" /proc/cpuinfo', shell=True, text=True
    ).strip()
    for inst in ["avx512", "avx2", "avx", "sse4"]:
        if re.search(inst, cpuinfo) is not None:
            break
    return (platform, model_name, inst)
