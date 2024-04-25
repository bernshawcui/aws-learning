## Amazon FSx
- 3rd party file systems managed by AWS

### FSx for Windows File Server
- Fully managed Windows file system share drive
- Supports SMB protocol & Windows NTFS
- Microsoft Active Directory integration, ACL, user quotas
- Can be mounted on linux EC2 instance
- Can be joined with on-prem Windows File System via Microsoft Distributed File System (DFS) Namespaces
- Scale up to 10s of GB/s, millions of IOPs, 100s PB of data
- Storage options:
  - SSD
  - HDD
- Can be accessed from on-prem infrastructure (VPN/DirectConnect)
- Can be configured to by multi-AZ
- Data is backed up daily to S3


### FSx for Lustre (Linux + Cluster)
- Parallel distributed file system for large-scale computing
- For ML, HPC, Video processing, financial modelling, EDA
- Scale up to 100s of GB/s, millions of IOPs, sub-ms latencies (faster than Windows File System)
- SSD Or HDD
- Seamless integration with S3:
  - Can read S3 as a file system via FSx
  - Can write output directly to S3
- Can be used from on-prem (VPN/DX)

Deployment Mode:
- Scrach File System:
  - Temporary storage, data is not replicated
  - If file server fails, data is lost
  - High burst (6x faster, 200MBps per TiB)
  - Usage: short-term processing, optimise cost and speed
- Persistent File System
  - Long-term storage, data is replicated within the same AZ
  - Replaced failed files within minutes
  - Usage: long-term processing, sensitive data


### NetApp ONTAP
- File system compatible with NFS, SMB, iSCSI protocol
- For workloads running on ONTAP/NAS to AWS
- Widely comptabilty with all OS, VMware cloud on AWS etc
- Shrinks and grows automatically
- Snapshots, replication, low-cost, compression and data de-duplication
- Point-in-time instantaneous cloning (helpful for testing new workloads)


### OpenZFS
- Compatible with NFS
- Up to 1 million IOPs with < 0.5ms latency
- Point-in-time instantaneous cloning (helpful for testing new workloads)