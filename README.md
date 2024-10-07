
		--------- Take-Home Challenge Documentation by Mélik Sevestre ---------

    --------------------------------
      DOCKER RUN COMMAND
    --------------------------------

  docker run -p 8080:8080 flask-nsjail-api

    --------------------------------	
     GCR cURL REQUEST -- FOR WINDOWS
    --------------------------------
    
curl -X POST -H "Content-Type: application/json" -d "{\"script\": \"def main(): return {\\\"message\\\": \\\"It works now Ruben!\\\"}\"}" "https://flask-nsjail-container-282247207309.europe-west1.run.app/execute"

    --------------------------------	
      GCR cURL REQUEST -- FOR MACOS
    --------------------------------

  curl -X POST https://flask-nsjail-container-282247207309.europe-west1.run.app/execute \
  -H "Content-Type: application/json" \
  -d '{"script": "def main():\n    return {\"message\": \"Hello Alexis ;)!\"}\n"}'

    --------------------------------	
     Time to complete the challenge
    --------------------------------
    
  ~5h

