import { registry } from "@web/core/registry";

import { Component } from "@odoo/owl";

console.log("🚀 ~ TODOClientAction...");
class TODOClientAction extends Component {
  static template = "todo_app.clientaction";
}

// remember the tag name we put in the first step
registry.category("actions").add("todo_app.TODOClientAction", TODOClientAction);
