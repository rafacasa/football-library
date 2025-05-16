window.addEventListener('load', (event) => {
    // get form template and total number of forms from management form
    const templateForm = document.getElementById('id_formset_empty_form');
    const inputTotalForms = document.querySelector('input[id$="-TOTAL_FORMS"]');
    const inputInitialForms = document.querySelector('input[id$="-INITIAL_FORMS"]');

    // get our container (e.g. <table>, <ul>, or <div>) and "Add" button
    const containerFormSet = document.getElementById('id_formset_container');
    const buttonAdd = document.getElementById('id_formset_add_button');
    const buttonSubmit = document.getElementById('id_formset_submit_button');

    // event handlers
    buttonAdd.onclick = addForm;


    function addForm () {
        // get new index
        new_index = Number(inputTotalForms.value)

        // create DocumentFragment from template
        const formFragment = templateForm.content.cloneNode(true);
        // a django form is rendered as_table (default), as_ul, or as_p, so
        // the fragment will contain one or more <tr>, <li>, or <p> elements,
        // respectively.
        for (let element of formFragment.children) {
            // replace the __prefix__ placeholders from the empty form by the
            // actual form index
            element.innerHTML = element.innerHTML.replace(
            /(?<=\w+-)(__prefix__|\d+)(?=-\w+)/g,
            new_index.toString());

            console.log(element)
        }
        containerFormSet.appendChild(formFragment);
        inputTotalForms.value = new_index + 1;
        // TENTAR AJUSTAR O ID DO BOTAO DE DELETE
    }
}, false);
