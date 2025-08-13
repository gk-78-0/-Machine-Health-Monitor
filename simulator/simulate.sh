#!/bin/bash

# Change these as needed
BACKEND_URL="http://backend:5000/telemetry"
MACHINE_ID="MRI_001"
HOSPITAL="City Hospital"

while true; do
  TEMPERATURE=$(awk "BEGIN {print 60 + (20 * rand())}")
  RUNTIME=$((RANDOM % 1500))
  STATUS="Running"
  ERROR_CODE="E$(($RANDOM % 200 + 100))"

  # Build JSON payload
  PAYLOAD=$(cat <<EOF
{
    "machine_id": "$MACHINE_ID",
    "hospital": "$HOSPITAL",
    "temperature": $TEMPERATURE,
    "runtime_hours": $RUNTIME,
    "status": "$STATUS",
    "error_code": "$ERROR_CODE"
}
EOF
)

  # Send telemetry
  curl -s -X POST -H "Content-Type: application/json" -d "$PAYLOAD" "$BACKEND_URL"

  sleep 10 # Send every 10 seconds
done