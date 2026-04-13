# 🚀 Serverless EBS gp2 → gp3 Automation Pipeline

## 📌 Overview

This project automates the detection and conversion of Amazon EBS `gp2` volumes to `gp3` using a fully serverless AWS architecture. It uses AWS managed services for scheduling, orchestration, logging, notifications, and audit tracking.

## 🎯 Objectives

* Detect EBS volumes with type `gp2`
* Filter only tagged volumes: `AutoConvert=true`
* Convert eligible volumes to `gp3`
* Verify modification status
* Store logs in DynamoDB
* Send SNS notifications
* Run automatically on schedule

---

## 🏗️ Architecture

**Workflow:**

1. EventBridge triggers daily schedule
2. Step Functions starts execution
3. ScanVolumes Lambda finds eligible volumes
4. Map state processes each volume
5. ConvertVolume modifies gp2 → gp3
6. Wait state pauses execution
7. VerifyVolume checks status
8. LogToDynamoDB stores audit trail
9. NotifySNS sends alerts
10. CloudWatch stores logs and metrics

---

## 🧰 AWS Services Used

* Amazon EC2 / EBS
* AWS Lambda
* AWS Step Functions
* Amazon EventBridge
* Amazon DynamoDB
* Amazon SNS
* Amazon CloudWatch
* AWS IAM

---

## 📁 Project Structure

```text
.
├── lambdas/
│   ├── scan_volumes.py
│   ├── convert_volume.py
│   ├── verify_volume.py
│   ├── log_to_dynamodb.py
│   └── notify_sns.py
├── stepfunctions/
│   └── workflow.json
├── screenshots/
├── architecture-diagram.png
└── README.md
```

---

## ⚙️ Deployment Steps

### 1. Create DynamoDB Table

Table Name: `EBSVolumeLogs`

* Partition Key: `VolumeId`
* Sort Key: `Timestamp`

### 2. Create SNS Topic

Create topic and subscribe email endpoint.

### 3. Create IAM Roles

Grant least-privilege permissions for Lambda and Step Functions.

### 4. Deploy Lambda Functions

Create 5 Lambda functions and upload code from `lambdas/` folder.

### 5. Create Step Function

Use `stepfunctions/workflow.json` definition.

### 6. Create EventBridge Rule

Schedule: `rate(1 day)`

---

## 🔐 Security Best Practices

* IAM roles instead of access keys
* Least privilege permissions
* Scoped access to specific resources
* CloudWatch logging enabled
* Encryption at rest for DynamoDB/EBS
* Error handling and retries

---

## 📊 Sample DynamoDB Record

```json
{
  "VolumeId": "vol-123456",
  "Timestamp": "2026-04-13T08:30:00Z",
  "InstanceId": "i-123456",
  "OldType": "gp2",
  "NewType": "gp3",
  "Status": "completed"
}
```

---

## 📬 Sample SNS Notification

```text
Subject: EBS Volume Converted
Volume ID: vol-123456
Status: completed
```
