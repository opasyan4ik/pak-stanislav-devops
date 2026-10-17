# Pak Stanislav DevOps Laboratory

An individual DevOps laboratory project that demonstrates Linux file and process commands, Git workflow, a small Python web application, Docker, Docker Compose, and a Jenkins Pipeline.

## Student

- Name: Stanislav
- Surname: Pak
- Group: IT2-2314
- Student ID: 37845
- Course: DevOps

## Project layout

```text
app/       Python application
config/    Application configuration
logs/      Demo log (generated locally and ignored by Git)
scripts/   Linux setup and system information scripts
tests/     Automated checks used by Jenkins
backup/    Ignored demonstration directory
```

## Run locally

From the project directory in Ubuntu or WSL:

```bash
bash scripts/setup_demo.sh
bash scripts/check_project.sh
python3 -m app.main
```

Open `http://localhost:8080/` for the student information and `http://localhost:8080/health` for the health check. Stop the app with Ctrl+C.

## Docker

```bash
docker build -t pak-stanislav-devops .
docker run -d --name pak-stanislav-container -p 8081:8080 \
  -e STUDENT_NAME=Stanislav -e STUDENT_SURNAME=Pak \
  -e STUDENT_GROUP=IT2-2314 -e STUDENT_ID=37845 \
  pak-stanislav-devops
curl http://localhost:8081/
docker logs pak-stanislav-container
docker rm -f pak-stanislav-container
```

Docker Compose starts the same application at `http://localhost:8081/` with `docker compose up -d` and stops it with `docker compose down`. Port 8081 avoids a conflict with Jenkins on its default port 8080.

## Jenkins

The public GitHub repository is `https://github.com/opasyan4ik/pak-stanislav-devops`. The Jenkins Pipeline job is named `Pak_Stanislav_DevOps` and uses this repository with “Pipeline script from SCM” and `Jenkinsfile` as the script path. The Jenkins agent needs Git, Python 3, Docker CLI, and permission to access the Docker daemon.

The Pipeline runs Checkout, Build, Test, Docker Build, and Docker Run stages. It prints the configured student data and the Git commit used by the job.

