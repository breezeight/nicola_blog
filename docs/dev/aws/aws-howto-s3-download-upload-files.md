# AWS S3 Download and Upload Files

## HOWTO download a directory from S3

To download an entire directory (or folder) from S3, use the following command:

* Using `cp` command to copy all files from the specified S3 directory to your local directory recursively:

```bash
aws s3 cp s3://your-bucket-name/path/to/directory ~/local-directory --recursive
```


* Alternatively, you can use the `sync` command, which is particularly useful for keeping directories in sync between S3 and your local machine, ensuring that only new or modified files are downloaded:

```bash
aws s3 sync s3://your-bucket-name/path/to/directory ~/local-directory
```

### Additional Options: Dry Run 

* Dry Run: If you want to see what would happen without actually downloading files, you can add the `--dry-run` flag:

```bash
aws s3 cp s3://your-bucket-name/path ~/local-directory --recursive --dry-run
```

### Additional Options: filtering

* Filtering Files: To download specific file types, you can use `--exclude` and `--include` flags:

```bash
aws s3 cp s3://your-bucket-name/path ~/local-directory --recursive --exclude "*" --include "*.csv"
```