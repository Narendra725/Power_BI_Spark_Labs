# class for the PowerBI Report
class PowerBIReport:
    def __init__(self, report_id, report_name, dataset_id):
        self.report_id = report_id
        self.report_name = report_name
        self.dataset_id = dataset_id

    def __str__(self):
        return f"PowerBIReport(report_id={self.report_id}, report_name={self.report_name}, dataset_id={self.dataset_id})"