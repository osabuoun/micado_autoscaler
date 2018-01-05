class Experiment:
    def __init__(self, id , name):
		experiment_id 	= id

		service_name	= name
		jqueuer_worker_added_count				=	0
	
		jqueuer_job_added_count					=	0
		jqueuer_job_running_count				=	0

		jqueuer_task_running_count				=	0
		jqueuer_task_accomplished_count			=	0
		jqueuer_task_accomplished_latency		=	0
		jqueuer_task_accomplished_latency_count	=	0
		jqueuer_task_accomplished_latency_sum	=	0

		jqueuer_job_accomplished_count			=	0
		jqueuer_job_accomplished_latency		=	0
		jqueuer_job_accomplished_latency_count	=	0
		jqueuer_job_accomplished_latency_sum	=	0

	def update(self, query_var, data):
