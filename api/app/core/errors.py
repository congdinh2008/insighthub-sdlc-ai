"""Public errors contain fixed messages, never provider bodies or credentials."""


class ServiceError(Exception):
    status_code = 500
    code = "internal_error"
    message = "Không thể xử lý yêu cầu."

    def __init__(self, message: str | None = None):
        if message is not None:
            self.message = message
        super().__init__(self.message)


class ProviderError(ServiceError):
    status_code = 502
    code = "provider_error"
    message = "Dịch vụ AI không khả dụng hoặc trả dữ liệu không hợp lệ."


class ProviderTimeout(ProviderError):
    status_code = 504
    code = "provider_timeout"
    message = "Dịch vụ AI không phản hồi trong thời gian cho phép."


class InvalidDocument(ServiceError):
    status_code = 422
    code = "invalid_document"
    message = "Tài liệu trống, không hợp lệ hoặc không có nội dung văn bản."


class DocumentNotFound(ServiceError):
    status_code = 404
    code = "document_not_found"
    message = "Không tìm thấy tài liệu."


class DocumentConflict(ServiceError):
    status_code = 409
    code = "document_conflict"
    message = "Document ID đã gắn với nội dung hoặc cấu hình xử lý khác."


class IndexIdentityConflict(ServiceError):
    status_code = 409
    code = "index_identity_conflict"
    message = (
        "Embedding identity không khớp index. Cần rebuild index bằng cấu hình đã chọn."
    )


class SchemaMismatch(ServiceError):
    status_code = 503
    code = "schema_mismatch"
    message = "Schema chưa sẵn sàng hoặc dimension không khớp EMBEDDING_DIM."


class IdempotencyKeyRequired(ServiceError):
    status_code = 400
    code = "idempotency_key_required"
    message = "Thiếu Idempotency-Key hợp lệ."


class IdempotencyConflict(ServiceError):
    status_code = 409
    code = "idempotency_conflict"
    message = "Idempotency-Key đã được dùng cho payload khác."


class OperationInProgress(ServiceError):
    status_code = 409
    code = "operation_in_progress"
    message = "Operation đang được xử lý."


class OperationNotFound(ServiceError):
    status_code = 404
    code = "operation_not_found"
    message = "Không tìm thấy operation còn hiệu lực."


class DeadlineExceeded(ServiceError):
    status_code = 504
    code = "deadline_exceeded"
    message = "Operation vượt quá thời gian xử lý cho phép."


class CitationValidationError(ServiceError):
    status_code = 502
    code = "citation_validation_failed"
    message = "Câu trả lời có citation không hợp lệ."


class SourceSetInvalid(ServiceError):
    status_code = 422
    code = "source_set_invalid"
    message = "Danh sách tài liệu nguồn không hợp lệ hoặc chưa sẵn sàng."
