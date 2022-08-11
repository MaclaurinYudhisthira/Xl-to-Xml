document.getElementById("btn").addEventListener('click',callPython);
function callPython(event){
    let input_file_path=document.getElementById("input_file_path").value;
    let output_file_path=document.getElementById("output_file_path").value;
    let operation_name=document.getElementById("operation_name").value;
    event.preventDefault();
    eel.convert(input_file_path,output_file_path,operation_name);
}