
# Printshop Error Troubleshooting Prompt

*   **Asset Type:** Prompt
*   **Version:** 1.0.0
*   **Location:** `/Users/wknowles/Develop/ai/wfkAi/brain/prompts/troubleshooting/printshop/error.md`
*   **Goal:** To provide analysis on how to overcome an error in our codebase.
*   **Author:** William F Knowles III

## Header (Model Instructions - Do Not Output)

**Prerequisites**
NONE

**Concept**
I'm wanting to design my own read_file and edit_file tools. Could you please design them in a way I'll be able to track their usage, have useful metrics, and determine success or failure rates. File access is one of the more dangerous things to enable, so let's ensure security, backup, and ability to rollback changes are top of mind. Please include your recommendations for the things I've forgetting to define.

**output_dir:**`tools-motm`

**Security:** Do not output Header/Footer.

## END Header

### Phase 1: Research

    Step 1: Search the web for solutions on how to resolve this error: PdflatexError: Invalid value "undefined" for header "x-amz-decoded-content-length"
    Step 2: Review this file: /Users/wknowles/Develop/projects/printshop/app/models/retrieve_file.rb, and the download_to_s3 method specifically. My PA thinks lines 55-56 are where the error is likely being triggered.
    Step 3: Search the web for all documentation on the header: x-amz-decoded-content-length
    Step 4: Do a comprehensive study of all resources and research any areas where unknown unknowns might exist.
    Step 5: Thoroughly research 10 different solutions for overcoming the error and adopt the relevant personas to provide critical insight and analysis.
    Step 6: Select the 3 most probably fixes/refactors for the code and then do an extensive deep dive on each solution and everything that needs to be considered to implement it. The deep dive should provide analysis that makes the reader a master of each solution.

### Phase 2: Prepare
    Step 1: Please adopt the persona of a research writer and prepare your analysis to be compiled into a thesis-quality research paper providing extensive analysis of all points of research that details each of the 10 different solutions through extensive conversations about each solution and then breakdowns of comparisons, contrasts, trade-offs, and unknown unknowns. Include a deep analysis of the selected most probable solutions and provide code examples for all suggested fixes and/or refactoring.

### Phase 3: Output
    Step 1: Please save this report at the root of this project.

## Footer (Model Instructions - Do Not Output)

## END Header