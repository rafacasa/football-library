window.addEventListener('load', (event) => {
    // get form template and total number of forms from management form
    const templateForm = document.getElementById('id_formset_empty_form');
    const inputTotalForms = document.querySelector('input[id$="-TOTAL_FORMS"]');

    // get our container (e.g. <table>, <ul>, or <div>) and "Add" button
    const containerFormSet = document.getElementById('id_formset_container');
    const buttonAdd = document.getElementById('id_formset_add_button');

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
        }
        containerFormSet.appendChild(formFragment);
        inputTotalForms.value = new_index + 1;
    }


}, false);

function deleteFoul(id_text) {
    var id_form = id_text.split("-")[1];
    console.log(id_form);

    template = document.getElementById('id_formset_delete_input_template');
    deleteFragment = template.content.cloneNode(true);

    for (let element of deleteFragment.children) {
        console.log(element.innerHTML);
        element.innerHTML = element.innerHTML.replace(
            /(?<=\w+-)(__prefix__|\d+)(?=-\w+)/g,
            id_form.toString());
        console.log(element);
    }
    var teste = document.getElementById(`div_id_game_foul_set-${id_form}-foul`)
    var linha = teste.parentElement.parentElement
    linha.appendChild(deleteFragment);
    linha.hidden = true;
}
