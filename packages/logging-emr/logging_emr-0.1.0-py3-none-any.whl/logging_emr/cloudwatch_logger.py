import logging
import argparse
import boto3
import sys
from datetime import datetime

class CloudWatchHandler(logging.Handler):
    """Handler para envio de logs ao AWS CloudWatch"""

    def __init__(self, log_group: str, log_stream: str, region_name="us-east-1"):
        super().__init__()
        self.client = boto3.client("logs", region_name=region_name)
        self.log_group = log_group
        self.log_stream = log_stream

    def get_sequence_token(self):
        """Obtém o sequence token necessário para enviar logs"""
        try:
            response = self.client.describe_log_streams(
                logGroupName=self.log_group, logStreamNamePrefix=self.log_stream
            )
            streams = response.get("logStreams", [])
            if streams:
                return streams[0].get("uploadSequenceToken")
        except Exception as e:
            print(f"Erro ao obter sequence token: {e}")
        return None

    def emit(self, record):
        """Envia os logs automaticamente para o CloudWatch"""
        try:
            message = self.format(record)
            timestamp = int(datetime.utcnow().timestamp() * 1000)
            log_event = {
                "logEvents": [{"timestamp": timestamp, "message": message}]
            }
            sequence_token = self.get_sequence_token()
            if sequence_token:
                log_event["sequenceToken"] = sequence_token

            self.client.put_log_events(
                logGroupName=self.log_group,
                logStreamName=self.log_stream,
                **log_event
            )
        except Exception as e:
            print(f"Erro ao enviar log: {e}")


def parse_args():
    """Faz o parsing dos argumentos da linha de comando"""
    parser = argparse.ArgumentParser(description="Configuração do Logger para CloudWatch")
    parser.add_argument("--logprocessorname", required=True, help="Nome do processador")
    parser.add_argument("--logstepname", required=True, help="Nome da step")
    return parser.parse_args()


def setup_logger():
    """Configura o logger para envio de logs ao AWS CloudWatch"""
    args = parse_args()

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("ProcessorLogger")

    cloudwatch_handler = CloudWatchHandler(args.logprocessorname, args.logstepname)
    logger.addHandler(cloudwatch_handler)

    # Tratamento de exceções globais
    def handle_exception(exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        logger.error("Exceção não tratada", exc_info=(exc_type, exc_value, exc_traceback))

    sys.excepthook = handle_exception

    return logger
