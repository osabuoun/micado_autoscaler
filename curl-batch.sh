
URL='http://185.12.7.200:9090'
PATH="/api/v1/query?query="

declare -a arr=("sum(jqueuer_job_accomplished_count)+by+(experiment_id,service_name)"
				"avg(jqueuer_job_accomplished_latency)+by+(experiment_id,service_name)"				 
				"sum(jqueuer_job_accomplished_latency_count)+by+(experiment_id,service_name)"				 
				"avg(jqueuer_job_accomplished_latency_sum)+by+(experiment_id,service_name)"				 
				"sum(jqueuer_job_added_count)+by+(experiment_id,service_name)"				 
				"sum(jqueuer_job_running_count)+by+(experiment_id,service_name)"				 
				"sum(jqueuer_task_accomplished_count)+by+(experiment_id,service_name,job_id)"				 
				"avg(jqueuer_task_accomplished_latency)+by+(experiment_id,service_name,job_id)"				 
				"sum(jqueuer_task_accomplished_latency_count)+by+(experiment_id,service_name,job_id)"				 
				"avg(jqueuer_task_accomplished_latency_sum)+by+(experiment_id,service_name,job_id)"				 
				"sum(jqueuer_task_running_count)+by+(experiment_id,service_name,job_id)"				 
				"sum(jqueuer_worker_added_count)+by+(experiment_id)"				 
				"sum(jqueuer_job_accomplished_count)+by+(experiment_id,service_name)"				 
                )
for i in "${arr[@]}"
do
   CURL_STRING=$URL$PATH$i
   echo $CURL_STRING
   #/usr/bin/curl $CURL_STRING
   #echo ""
   #echo "--------------------------------------------------------------"
   # or do whatever with individual element of the array
done


