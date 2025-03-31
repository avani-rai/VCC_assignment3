# Get CPU usage
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk -F'[, ]+' '{print 100 - $8}')

echo "CPU Usage: $CPU_USAGE%"

# Check if CPU usage exceeds 75%
if (( $(echo "$CPU_USAGE > 75" | bc -l) )); then
    echo "CPU usage exceeded 75%. Creating a new VM in GCP..."

    # Ensure project is set
    PROJECT_ID="gcp-vm-452503"  # project ID
    gcloud config set project $PROJECT_ID

    # Create a new VM instance
    gcloud compute instances create scaled-vm-$(date +%s) \
        --zone=us-central1-a \
        --machine-type=n1-standard-1 \
        --image-family=ubuntu-2004-lts \
        --image-project=ubuntu-os-cloud \
        --project=$PROJECT_ID
fi
