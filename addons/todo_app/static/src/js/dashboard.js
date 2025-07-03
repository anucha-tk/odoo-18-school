import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

console.log("🚀 ~ TODOClientAction...");

class TODOClientAction extends Component {
  static template = "todo_app.clientaction";
  setup() {
    super.setup();
    console.log("🚀 ~ TODOClientAction: Component setup completed.");
    this.state = useState({
      tasks: [],
      loading: true,
      error: null,
    });
    this.loadTodo();
  }

  async loadTodo() {
    this.state.loading = true;
    this.state.error = null;
    try {
      console.log("🚀 ~ TODOClientAction ~ loadPartners ~ Fetching data from /todo/data...");
      const result = await rpc("/todo/data");
      console.log("🚀 ~ TODOClientAction ~ loadPartners ~ result:", result);

      if (result && Array.isArray(result.todo)) {
        this.state.tasks = result.todo;
      } else {
        console.warn("🚀 ~ /todo/data did not return an array for 'todo':", result);
        this.state.tasks = [];
      }
    } catch (error) {
      console.error("🚀 ~ Error fetching data:", error);
      this.state.error = "Failed to load data: " + (error.message || "Unknown error");
    } finally {
      this.state.loading = false;
    }
  }
}

registry.category("actions").add("todo_app.TODOClientAction", TODOClientAction);
