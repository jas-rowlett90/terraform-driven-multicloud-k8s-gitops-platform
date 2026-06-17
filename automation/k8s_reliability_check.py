#!/usr/bin/env python3

import json
import subprocess
import sys
from datetime import datetime, UTC

NAMESPACES_TO_CHECK = ["default", "monitoring", "argocd"]


def run_kubectl(args):
    command = ["kubectl"] + args

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"ERROR running command: {' '.join(command)}")
        print(result.stderr)
        sys.exit(1)

    return result.stdout.strip()


def get_json(args):
    output = run_kubectl(args + ["-o", "json"])
    return json.loads(output)


def check_pods(namespace):
    pod_data = get_json(["get", "pods", "-n", namespace])

    results = []

    for pod in pod_data.get("items", []):

        name = pod["metadata"]["name"]
        phase = pod["status"].get("phase", "Unknown")

        container_statuses = pod["status"].get("containerStatuses", [])

        ready = all(
            container.get("ready", False)
            for container in container_statuses
        )

        restart_count = sum(
            container.get("restartCount", 0)
            for container in container_statuses
        )

        issues = []

        if phase not in ["Running", "Succeeded"]:
            issues.append(f"Pod phase is {phase}")

        if not ready and phase != "Succeeded":
            issues.append("One or more containers are not ready")

        if restart_count >= 3:
            issues.append(f"Restart count is {restart_count}")

        results.append(
            {
                "namespace": namespace,
                "pod": name,
                "phase": phase,
                "ready": ready,
                "restart_count": restart_count,
                "healthy": len(issues) == 0,
                "issues": issues
            }
        )

    return results


def check_deployments(namespace):
    deployment_data = get_json(
        ["get", "deployments", "-n", namespace]
    )

    results = []

    for deployment in deployment_data.get("items", []):

        name = deployment["metadata"]["name"]

        desired = deployment["spec"].get("replicas", 0)

        available = deployment["status"].get(
            "availableReplicas",
            0
        )

        issues = []

        if available < desired:
            issues.append(
                f"Available replicas {available} below desired {desired}"
            )

        results.append(
            {
                "namespace": namespace,
                "deployment": name,
                "desired_replicas": desired,
                "available_replicas": available,
                "healthy": len(issues) == 0,
                "issues": issues
            }
        )

    return results


def main():

    report = {
        "generated_at": datetime.now(UTC).isoformat(),
        "checked_namespaces": NAMESPACES_TO_CHECK,
        "pods": [],
        "deployments": [],
        "summary": {}
    }

    for namespace in NAMESPACES_TO_CHECK:
        report["pods"].extend(check_pods(namespace))
        report["deployments"].extend(
            check_deployments(namespace)
        )

    unhealthy_pods = [
        pod
        for pod in report["pods"]
        if not pod["healthy"]
    ]

    unhealthy_deployments = [
        deployment
        for deployment in report["deployments"]
        if not deployment["healthy"]
    ]

    report["summary"] = {
        "total_pods_checked": len(report["pods"]),
        "unhealthy_pods": len(unhealthy_pods),
        "total_deployments_checked": len(
            report["deployments"]
        ),
        "unhealthy_deployments": len(
            unhealthy_deployments
        ),
        "overall_status": (
            "healthy"
            if not unhealthy_pods
            and not unhealthy_deployments
            else "unhealthy"
        )
    }

    with open(
        "reliability_report.json",
        "w"
    ) as f:
        json.dump(report, f, indent=2)

    print(json.dumps(report, indent=2))

    print(
        "\nReliability report written to reliability_report.json"
    )

    if report["summary"]["overall_status"] != "healthy":
        sys.exit(1)


if __name__ == "__main__":
    main()
