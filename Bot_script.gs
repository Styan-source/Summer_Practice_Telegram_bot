function doPost(e) {
  var update = JSON.parse(e.postData.contents);
  var sheet =  SpreadsheetApp.openById('ЗАКРЫЛ ТОКЕН').getSheets()[0]
  var arraysCommands = sheet.getRange(2, 4, sheet.getLastRow() - 1).getValues();
  var arrayCommands = arraysCommands.map(function (row){return row[0]})
  if (update.hasOwnProperty('message')) {
    var msg = update.message;
    var chatId = msg.chat.id;
    var numRow = arrayCommands.indexOf(msg.text) + 2; 
    if (msg.hasOwnProperty('entities') && msg.entities[0].type == 'bot_command') {
        var lastpost = sheet.getRange(numRow, 2, 1,  3).getValues()[0]
        var message = ' <strong>'+lastpost[1] + '</strong> \n' + lastpost[2]
       
        var payload = {
          'method': 'sendMessage',
          'chat_id': String(chatId),
          'text': message,
          'parse_mode': 'HTML'
        }     
        var data = {
          "method": "post",
          "payload": payload
        }
        
        var API_TOKEN = 'ЗАКРЫЛ ТОКЕН'
        UrlFetchApp.fetch('https://api.telegram.org/bot' + API_TOKEN + '/', data);
      }
    }
}
