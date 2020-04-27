![Blender Render Manager](https://www.joaulo.com/media/projects/project_blender-render-manager-blender-addon/preview_big.jpg)
# blender-render-manager

Questo addon nasce dalla esigenza di renderizzare durante la notte un certo numero di telecamere inserite nella scena.

Attualmente ha una serie di limitazioni per questo motivo ha la sua utilità in un contesto specifico, ma vorrei farlo crescere in futuro espandendo le possibilità di utilizzo.

# Installazione

Si installa come un normale addon di Blender, basta scaricare il file .zip sul proprio PC, quindi da Blender > Edit > Preferences... seguire la installazione tradizionale. Per maggiori informazioni potete fare riferimento alla pagina di manuale di Blender.

# Come funziona?

Una volta installato ed attivato, l'interfaccia dell'addon sarà visibile in un pannello dedicato chiamato "Render Manager" nella sezione "Output Properties":

![Render Manager Panel](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_191102.jpeg)

Nell'ordine dall'alto al basso:

* Render output: selezionare la cartella dove si vuole salvare i render
* Select a collection: selezionare dalla lista una Collezione contentente una o più telecamere
* Render Manager::Images : pulsante per avvio render di immagini statiche (al frame attuale) in sequenza su tutte le telecamere rilevate nella Collezione selezionata ed in tutte le sotto-collezioni
* Render Manager::Animations : pulsante per avvio render di animazioni in sequenza su tutte le telecamere rilevate nella Collezione selezionata ed in tutte le sotto-collezioni

È possibile salvare le impostazioni di rendering in un file e ricaricarle in un secondo momento prima di lanciare i render. Per farlo, si utlizzano i pannelli sottostanti:

* Load Settings
* Save Settings

In entrambe i pannelli è presente un campo in cui è possibile selezionare il percorso ed il file in cui andare a caricare/salvare le impostazioni di render.

# Limitazioni e problemi noti

* non è possibile utilizzare impostazioni di render differenti per i render lanciati in sequenza sulle varie telecamere trovate in una collezione! Si suggerisce di raggruppare le telecamere in collezioni differenti a seconda delle impostazioni di render. Come conseguenza all'utilizzo delle medesime impostazioni, anche i render delle animazioni iniziano e finiscono dagli stessi frames.
* non utilizzare il percorso relativo nelle selezioni di files o cartelle all'interno dell'addon, utilizzate solo percorsi assoluti! A causa di un problema non ancora risolto, utilizzando il percorso relativo il file o la cartella non verranno trovati risultando in un messaggio di errore all'esecuzione del comando. Per utilizzare i percorsi assoluti, dopo aver cliccato sull'icona a forma di cartella di fianco al campo di selezione, utilizzare le seguenti impostazioni nella finestra di selezione del percorso:

   * *selezionare l'icona a forma di ingranaggio in alto a destra:*
   
   ![path settings](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211442.jpeg)

   * *disattivare il checkbox:*
   
   ![checkbox_wrong](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211522.jpeg)
   ![checkbox_right](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211731.jpeg)

   * *verificare che il percorso nel campo sia il percorso completo del file:*
   
   ![full_path](https://www.joaulo.com/media/uploads/2020/04/26/screenshot_20200426_211802.jpeg)

# TO DO

* salvare impostazioni differenti per ogni telecamera
* caricare impostazioni specifiche per ogni telecamera prima di lanciare il render
