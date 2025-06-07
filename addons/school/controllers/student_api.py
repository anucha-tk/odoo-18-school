import json

from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request


class StudentApi(http.Controller):
    @http.route(
        "/api/v1/students",
        methods=["GET"],
        type="http",
        auth="none",
        csrf=False,
    )
    def list_students(self, **kwargs):
        try:
            page = int(kwargs.get("page", 1))
            limit = int(kwargs.get("limit", 10))
            gender = kwargs.get("gender")
            status = kwargs.get("status")
            order = kwargs.get("order", "id desc")  # default sort

            domain = []
            if gender:
                domain.append(("gender", "=", gender))
            if status:
                domain.append(("status", "=", status))

            offset = (page - 1) * limit
            students = (
                request.env["school.student"]
                .sudo()
                .search(domain, limit=limit, offset=offset, order=order)
            )
            total = request.env["school.student"].sudo().search_count(domain)

            data = [
                {
                    "id": s.id,
                    "name": s.name,
                    "age": s.age,
                    "gender": s.gender,
                    "status": s.status,
                    "teacher_id": s.teacher_id.id,
                }
                for s in students
            ]

            return http.Response(
                json.dumps(
                    {
                        "total": total,
                        "page": page,
                        "limit": limit,
                        "students": data,
                    }
                ),
                status=200,
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=500,
                content_type="application/json",
            )

    @http.route(
        "/api/v1/student/<int:student_id>",
        methods=["GET"],
        type="http",
        auth="none",
        csrf=False,
    )
    def get_student(self, student_id):
        try:
            student = request.env["school.student"].sudo().browse(student_id)
            if not student.exists():
                return http.Response(
                    json.dumps({"error": "Student not found"}),
                    status=404,
                    content_type="application/json",
                )

            data = {
                "id": student.id,
                "name": student.name,
                "age": student.age,
                "gender": student.gender,
                "status": student.status,
                "teacher_id": student.teacher_id.id,
            }

            return http.Response(
                json.dumps(data),
                status=200,
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=500,
                content_type="application/json",
            )

    @http.route(
        "/api/v1/student",
        methods=["POST"],
        type="http",
        auth="none",
        csrf=False,
    )
    def post_student(self):
        try:
            args = json.loads(request.httprequest.data.decode())
            required_fields = ["name", "age", "gender", "status"]
            # Check missing or empty values correctly:
            missing = [f for f in required_fields if not args.get(f)]
            if missing:
                return http.Response(
                    json.dumps(
                        {
                            "error": f"Missing required fields: {', '.join(missing)}"
                        }
                    ),
                    status=422,
                    content_type="application/json",
                )

            res = request.env["school.student"].sudo().create(args)
            return http.Response(
                json.dumps({"id": res.id, "status": "created"}),
                status=201,
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=500,
                content_type="application/json",
            )

    @http.route(
        "/api/v1/student/json",
        methods=["POST"],
        type="json",
        auth="none",
        csrf=False,
    )
    def post_student_json(self, **args):
        required_fields = ["name", "age", "gender", "status"]
        missing = [f for f in required_fields if not args.get(f)]
        if missing:
            # Raise an exception with status 422 for missing fields
            raise ValidationError(
                f"Missing required fields: {', '.join(missing)}"
            )

        try:
            res = request.env["school.student"].sudo().create(args)
            return {"id": res.id, "status": "created"}
        except Exception as e:
            return {"error": str(e)}

    @http.route(
        "/api/v1/student/<int:student_id>",
        methods=["PUT"],
        type="http",
        auth="none",
        csrf=False,
    )
    def update_student(self, student_id):
        try:
            student = request.env["school.student"].sudo().browse(student_id)
            if not student.exists():
                return http.Response(
                    json.dumps({"error": "Student not found"}),
                    status=404,
                    content_type="application/json",
                )

            args = json.loads(request.httprequest.data.decode())
            student.write(args)

            return http.Response(
                json.dumps({"id": student.id, "status": "updated"}),
                status=200,
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=500,
                content_type="application/json",
            )

    @http.route(
        "/api/v1/student/<int:student_id>",
        methods=["DELETE"],
        type="http",
        auth="none",
        csrf=False,
    )
    def delete_student(self, student_id):
        try:
            student = request.env["school.student"].sudo().browse(student_id)
            if not student.exists():
                return http.Response(
                    json.dumps({"error": "Student not found"}),
                    status=404,
                    content_type="application/json",
                )

            student.unlink()
            return http.Response(
                json.dumps({"status": "deleted"}),
                status=200,
                content_type="application/json",
            )
        except Exception as e:
            return http.Response(
                json.dumps({"error": str(e)}),
                status=500,
                content_type="application/json",
            )
