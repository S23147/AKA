document.getElementById("loadPatients").addEventListener("click", function() {
    fetch("/api/patients/")
        .then(response => response.json())
        .then(data => {
            let list = document.getElementById("patientList");
            list.innerHTML = "";
            data.patients.forEach(patient => {
                let li = document.createElement("li");
                li.className = "list-group-item";
                li.textContent = patient.nom + " " + patient.prenom;
                list.appendChild(li);
            });
        });
});

document.getElementById('addPatientForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let formData = new FormData(this);
    fetch("/api/add_patient/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Patient ajouté avec succès !");
            location.reload();
        } else {
            alert("Erreur : " + JSON.stringify(data.errors));
        }
    });
});
