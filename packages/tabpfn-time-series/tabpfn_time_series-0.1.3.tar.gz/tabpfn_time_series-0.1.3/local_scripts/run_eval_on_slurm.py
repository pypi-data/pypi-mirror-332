#!/usr/bin/env python3

# Add gift_eval to python path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import argparse
import submitit
from datetime import datetime

from gift_eval.dataset_definition import ALL_DATASETS


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate and run sbatch script for time series benchmark"
    )
    parser.add_argument(
        "--cluster_partition",
        default="mlhiwidlc_gpu-rtx2080-advanced",
        help="Cluster partition to use",
    )
    parser.add_argument(
        "--dataset",
        default="all",
        help="Dataset to run, either a single dataset or 'all'",
    )
    parser.add_argument("--ngpus", type=int, default=1, help="Number of GPUs to use")
    parser.add_argument(
        "--terms",
        type=str,
        help="Comma-separated list of terms to evaluate",
        default=None,
        required=False,
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    job_name = f"time_series_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    memory = 128
    num_cpus = 16
    num_gpus = args.ngpus

    gift_eval_script_path = Path(__file__).parent.parent / "gift_eval" / "evaluate.py"

    # If a single task is specified, check if it is valid
    if args.dataset != "all":
        if args.dataset not in ALL_DATASETS:
            raise ValueError(f"Dataset {args.dataset} not found in dataset definition")
        datasets = [args.dataset]
    else:
        datasets = ALL_DATASETS

    num_datasets = len(datasets)

    # Report the benchmark parameters
    print("\nRunning evaluation with the following parameters:")
    print(f" . CLUSTER_PARTITION: {args.cluster_partition}")
    print(f" . # GPUS: {num_gpus}")
    print(f" . # DATASETS: {num_datasets}")
    print(f" . DATASETS: {datasets}")

    # Setup submitit executor
    executor = submitit.AutoExecutor(folder=f"slurm_logs/{job_name}")
    executor.update_parameters(
        name=job_name,
        nodes=1,
        tasks_per_node=1,
        cpus_per_task=num_cpus,
        mem_gb=memory,
        slurm_gres=f"gpu:{num_gpus}",
        slurm_partition=args.cluster_partition,
        slurm_array_parallelism=num_datasets,
        slurm_setup=["source ~/.gift_eval_bashrc"],
        timeout_min=1439,  # 23 hours and 59 minutes
        slurm_additional_parameters={"exclude": "dlcgpu18,dlcgpu35,dlcgpu30"},
    )

    jobs = []
    with executor.batch():
        for dataset in datasets:
            cmd = ["python", str(gift_eval_script_path)]
            script_args = [
                "--model_name",
                "tabpfn-ts-paper",
                "--dataset",
                dataset,
                "--output_dir",
                f"slurm/{job_name}",
            ]

            if args.terms:
                script_args.append("--terms")
                script_args.append(args.terms)

            job = executor.submit(submitit.helpers.CommandFunction(cmd), *script_args)
            jobs.append(job)

    print(f"Submitted {len(jobs)} jobs")

    # # Wait for all jobs to complete
    # for job in jobs:
    #     job.result()


if __name__ == "__main__":
    main()
