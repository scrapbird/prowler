from providers.aws.lib.audit_info.audit_info import current_audit_info
from providers.aws.services.accessanalyzer.accessanalyzer_service import AccessAnalyzer

accessanalyzer_client = AccessAnalyzer(current_audit_info)
