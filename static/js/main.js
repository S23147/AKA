// Charger la liste des patients
document.getElementById("loadPatients").addEventListener("click", async function() {
    try {
        const response = await fetch("/api/patients/");
        if (!response.ok) {
            throw new Error("Erreur lors du chargement des patients");
        }

        const data = await response.json();
        let list = document.getElementById("patientList");
        list.innerHTML = "";  // Effacer la liste actuelle

        data.patients.forEach(patient => {
            let li = document.createElement("li");
            li.className = "list-group-item";
            li.textContent = `${patient.nom} ${patient.prenom}`;
            list.appendChild(li);
        });
    } catch (error) {
        console.error("Erreur:", error);
        alert("Impossible de charger la liste des patients. Veuillez réessayer.");
    }
});

// Ajouter un nouveau patient
document.getElementById('addPatientForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Empêcher le rechargement de la page
    let formData = new FormData(this);

    // Ajouter un indicateur de chargement
    const loadingIndicator = document.getElementById("loadingIndicator");
    loadingIndicator.style.display = "block";

    try {
        const response = await fetch("/api/add_patient/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (response.ok && data.success) {
            alert("Patient ajouté avec succès !");
            location.reload();  // Recharge la page pour afficher les nouveaux patients
        } else {
            throw new Error(data.errors ? JSON.stringify(data.errors) : "Erreur inconnue");
        }
    } catch (error) {
        console.error("Erreur lors de l'ajout du patient:", error);
        alert("Erreur : " + error.message);
    } finally {
        // Masquer l'indicateur de chargement après traitement
        loadingIndicator.style.display = "none";
    }
});
