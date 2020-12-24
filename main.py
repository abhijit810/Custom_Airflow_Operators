from customAirflowOperators import TriggerDagRunAndWaitOperator

task_etl_claims_pkg = TriggerDagRunAndWaitOperator( task_id='Task_Triggers_Dag_and_waits_for_it_to_complete', trigger_dag_id='DAG_Name_you_want_to_trigger', dag=dag, )