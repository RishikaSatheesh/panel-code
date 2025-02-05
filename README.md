# panel-code
This application, built using Panel and Param, allows users to select the number of shapes they want to provide dimensions for, dynamically generating input widgets accordingly.

How it works:

1. Select Number of Shapes: The user chooses the number of shapes in the sidebar.
2. Clicking the "Select" button triggers the get_dashboard function in rectangle.py file, updating the main tab with the corresponding input fields.
3. Input Dimensions: Once the tab is updated, users enter the required dimensions in the generated widgets.
4. Hit the "Submit" button on the tab which updates the Tabulator widget displaying user-selected dimensions, calculated area and perimeter.
