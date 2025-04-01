# ALOOF - Aloof Language Organization of Output Forms

**Status: Conceptual Language Definition**

## Introduction

ALOOF (Aloof Language Organization of Output Forms) is a conceptual Domain-Specific Language (DSL) designed for the high-level, abstract definition of form structures and their associated elements. It aims to simplify the initial design and definition phase by focusing purely on the essential components – layout, order, labels, types, validation rules – while remaining intentionally "aloof" from concrete implementation details and specific output formats.

*(Note: This concept originated from early ideas tentatively named User Level Up Form Language or ULUFL.)*

## Philosophy

The core idea behind ALOOF is to decouple the *structural and logical definition* of a form from its *final technical representation*. Often, the initial phase of defining a form gets bogged down in specifics like HTML `id`s, `name` attributes, CSS classes, or the exact syntax of the target platform. ALOOF provides a way to define the form's essence first, in a human-readable way, deferring the implementation specifics to a separate, automated process.

## Key Principles

1. Abstraction ("Aloofness"): The language syntax intentionally omits implementation details like specific IDs, names, values, CSS classes, ARIA attributes, etc. It focuses on the abstract concepts.

1. Separation of Concerns: ALOOF enforces a clear separation between:

1. Structural Definition (ALOOF): Defines order, labels, types, validation rules.

1. Implementation Details (Parallel Data): A separate data structure holds names, values, classes, styles, descriptions, etc.

1. Output Generation (Templates/Processor): A templating engine combines the ALOOF definition and parallel data to generate the final output.

1. Order-Based Mapping: The link between a line in an ALOOF definition and its corresponding implementation details in the parallel data structure is based strictly on their order.

1. Target Agnosticism: Because the ALOOF definition is abstract, the same definition can theoretically be used to generate different output formats (HTML, JSON, XML, UI definitions, backend code structures, etc.).

## Core Requirements (Distilled)
1. Line-Based Processing: Each line in ALOOF represents a distinct form element or a group of related elements.

1. Order Markers: Markers like [N] or [] are used to denote ordered or unordered structures.

1. Parallel Data: ALOOF uses a separate "parallel data" structure.

1. Excel Analogy: Each ALOOF line is like a cell in Excel, while adjacent cells store metadata.

1. Related Fields: Each ALOOF line defines related fields.

1. HTML Output: ALOOF generates HTML with <label>, <input>, and <span> for validation messages.

1. Submit Button: Special handling for submit buttons.

1. Loop Processing: Each line is processed sequentially.

1. Aloof Mindset: Ignore non-ALOOF columns when working with data in spreadsheets.

## Syntax Overview

ALOOF uses a simple, line-based syntax. Each line typically defines a form element or a configuration setting.

**Basic Element Syntax:**

[N] Label and Input Type (data type, validation_rules..., "error_message")(control_type)

- `[N]` or `[]`: Optional marker for ordered (`[1]`, `[2]`) or unordered (`[]`) structure.
- `Label and Input Type`: The user-facing label and type for the form element.
- `(data type, validation..., "message")`: Parentheses containing:  
- `data type`: A hint for the data type (e.g., `string`, `number`, `date`).  
- `validation_rules`: Keywords like `required`, or potentially patterns like `/regex/`.  
- `"error_message"`: The message to display if validation fails.
- `(control_type)`: Optional second set of parentheses hinting at the intended output widget type (e.g., `(text)`, `(date)`, `(submit)`).**Configuration Syntax:**

<pre>
[1] Label and Text Input (string, required, "This field is required.")(text)
[2] Label and Group of 3 Checkboxes (checkbox, unchecked)(checkbox)
[3] Label and 4 Radio Buttons (radio, default=1)(radio)
[] Submit Button (submit)
Summary Message Location: top
</pre>

**Bigger Example**
<pre>
[1] First Name (string, required, "First name is required.")(text)
[2] Last Name (string, required, "Last name is required.")(text)
[3] Username (string, required, /^[a-zA-Z0-9_]{4,16}$/, "Username must be 4-16 letters, numbers, or underscores.")(text)
[4] Email Address (string, required, /^[^\s@]+@[^\s@]+\.[^\s@]+$/, "Please enter a valid email address.")(email)
[5] Password (string, required, /.{8,}/, "Password must be at least 8 characters.")(password)
[6] Confirm Password (string, required, "Please confirm your password.")(password)
[7] Date of Birth (date, "Please enter your date of birth.")(date)
[8] Country (string, required, "Please select your country.")(select)
[9] Receive Newsletter (boolean, unchecked)(checkbox)
[10] Agree to Terms (boolean, required, checked, "You must agree to the terms to register.")(checkbox)
[] Register (submit)(submit)
</pre>

Explanation of Notable Lines:

<pre>
[3] Username: Includes a required validation and a regular expression (/^[a-zA-Z0-9_]{4,16}$/) to enforce specific character rules and length, along with a corresponding error message.
[4] Email Address: Similar to Username, uses required and a common regex for email format validation. The output hint (email) suggests using &lt;input type="email"&gt;.
[5] Password: Uses required and a simple regex (/.{8,}/) to enforce a minimum length. The output hint (password) suggests &lt;input type="password"&gt;.
[6] Confirm Password: Marked as required. Note that the logic to check if this matches the previous password field would typically reside in the template processing logic or client/server-side code, as ALOOF focuses on defining individual field rules.
[7] Date of Birth: This field is not marked required, making it optional. It uses the date type hint.
[8] Country: Marked required. The output hint (select) suggests this should be rendered as a dropdown/select list. The actual options for the list would need to be provided in the corresponding parallel data structure.
[9] Receive Newsletter: Uses a boolean type hint (representing true/false). The validation hint unchecked suggests its default state is false/off. It's optional. The output hint (checkbox) is appropriate.
[10] Agree to Terms: Also boolean, but marked required. The validation hint checked implies that this field must be true/checked for the form validation to pass.
</pre>

This example demonstrates how ALOOF could handle various common input types, validation rules (including regex), optional fields, and hints for specific HTML controls like &lt;select&gt; or &lt;input type="password"&gt;. Remember, this definition would need a corresponding parallel data structure providing names, IDs, default values, and crucially, the options list for the "Country" select field.

Summary Message Location: top

## Current Goal:

Focus on Alignment: The primary goal is to perform the alignment of ALOOF lines and their metadata.
JSON Output: Generate a JSON output that clearly shows the association between each ALOOF line and its metadata.
Easy Verification: The JSON output should be easy for anyone to verify that the alignment is correct.
HTML Output: We will continue to generate the HTML output.

**Summary Message Location:** Top

### Accompanying Parallel Data
The parallel data would contain meta data such as:
- `name: name_of_field`
- `name: task_desc`
- `name: creator_name`
- `name: creation_date`
- `name: submit_button`
- etc., in that order.

### Benefits
- **Simplified Initial Definition**: Makes defining the core form structure easier and more readable, especially for less technical users.
- **Rapid Prototyping**: Quickly sketch out form layouts without getting stuck on implementation details.
- **Strong Separation of Concerns**: Cleanly divides structure/validation, implementation details, and output generation.
- **Enforced Consistency**: Templating ensures consistent naming conventions, attribute usage, and accessibility basics.
- **Portability / Target Independence**: Define once, generate for multiple platforms (Web, mobile, API, backend) by changing templates.
- **Abstraction**: Hides the complexity of the target platform's specific syntax.

### Considerations / Drawbacks
- **Order Dependency Fragility**: The strict reliance on maintaining identical order between the ALOOF file and the parallel data structure is powerful but potentially fragile during maintenance. Reordering requires careful synchronization.
- **Tooling Required**: ALOOF definitions are not directly usable; they require a dedicated parser and templating engine to be useful.
- **Two-Step Process**: Introduces an intermediate definition layer compared to directly writing the final format.
- **Limited Expressiveness (by design)**: Complex UI interactions or highly dynamic form behaviors might be difficult to represent solely within ALOOF and may require more complex logic in the templating/processing stage or client-side scripting.

### Status
ALOOF is currently a conceptual language definition. No official parser or tooling exists at this time (as of March 31, 2025). This document describes the intended design and principles.
This should make your summary clear and well-organized. Let me know if you need any further adjustments!

Alignment example with its meta data:

JSON Output:
```json
{
  "form_elements": [
    {
      "aloof_line": "[1] First Name (string, required, \"First name is required.\")(text)",
      "metadata": {
        "line_1_name": "first_name",
        "line_1_id": "first-name-input",
        "line_1_class": "form-input"
      }
    },
    {
      "aloof_line": "[2] Last Name (string, required, \"Last name is required.\")(text)",
      "metadata": {
        "line_2_name": "last_name",
        "line_2_id": "last-name-input",
        "line_2_class": "form-input"
      }
    },
    {
      "aloof_line": "[] Register (submit)(submit)",
      "metadata": {
        "line_3_name": "register_button",
        "line_3_id": "register-button",
        "line_3_class": "form-button"
      }
    }
  ]
}
```

HTML Output:
```html
<label>1. First Name</label><input /><span data-validation="required">First name is required.</span><br />
<label>2. Last Name</label><input /><span data-validation="required">Last name is required.</span><br />
<label>Register</label><input type='submit' /><br />
```

ALOOF is a conceptual language focused on simplifying form definition. By separating concerns and abstracting implementation details, it enables rapid prototyping and enhances flexibility. While still in its early stages, further development on parsers, processors, and template engines will unlock ALOOF's full potential.

For any questions or contributions, please refer to the project repository at GitHub - ALOOF.