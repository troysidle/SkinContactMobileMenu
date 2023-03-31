function onOpen() {
  var ui = DocumentApp.getUi();
  ui.createMenu('Publish')
    .addItem('Publish', 'publishDocument')
    .addToUi();
}

function publishDocument() {
  var document = DocumentApp.getActiveDocument();
  var file = DriveApp.getFileById(document.getId());
  var fileName = "CurrentMenu.txt";
  var mimeType = MimeType.PLAIN_TEXT;
  
  // Create a copy of the document as a text file
  var textFile = file.makeCopy(fileName);
  var textContent = document.getBody().getText();
  textFile.setContent(textContent);
  
  // Update or create the PDF file
  var pdfFileName = "SkinContact_WineList.pdf";
  var pdfFile = null;
  var pdfBlob = null;
  var pdfFolder = DriveApp.getRootFolder(); // change this to desired folder if needed
  
  var existingFiles = pdfFolder.getFilesByName(pdfFileName);
  if (existingFiles.hasNext()) {
    pdfFile = existingFiles.next();
  }
  
  if (pdfFile) {
    // If the PDF file already exists, update it
    pdfBlob = pdfFile.getAs(MimeType.PDF);
    pdfBlob.setDataFromString(textContent, mimeType);
    pdfFile.setContent(pdfBlob);
  } else {
    // If the PDF file does not exist, create it
    pdfBlob = textFile.getAs(MimeType.PDF);
    pdfFile = pdfFolder.createFile(pdfBlob);
    pdfFile.setName(pdfFileName);
  }
  
  // Display a confirmation message to the user
  var ui = DocumentApp.getUi();
  ui.alert('Files created successfully!');
}





//or


function onOpen() {
  var ui = DocumentApp.getUi();
  ui.createMenu('publish')
      .addItem('Create Files', 'createFiles')
      .addToUi();
}

function createFiles() {
  var docName = "SkinContactWineList";
  var pdfName = "SkinContact_WineList.pdf";
  var sourceDoc = DocumentApp.getActiveDocument();
  var newDoc = sourceDoc.makeCopy(docName);
  var pdfFile = newDoc.getAs(MimeType.PDF);
  var parentFolder = DriveApp.getFileById(newDoc.getId()).getParents().next();
  var pdfFileID = parentFolder.createFile(pdfFile).setName(pdfName).getId();
  Logger.log("PDF file created with ID: " + pdfFileID);
}