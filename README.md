
		--------- Take-Home Challenge Documentation by Mélik Sevestre ---------

The project aimed to use "nsjail" for sandboxing (flask-nsjail-api). 
Due to deployment issues on Google Cloud Run, such as port conflicts and compatibility problems, I switched to "seccomp". (MAIN-flask-seccomp-api)
It still provides robust security while maintaining compatibility with Google Cloud Run’s managed environment.

Except for "nsjail" all criteria have been met.
The Challenge directory containing NsJail is located in the same GitHub Repo if needed !

    --------------------------------
      DOCKER RUN COMMAND
    --------------------------------

  docker run -p 8080:8080 flask-seccomp-api

    --------------------------------	
      GCR cURL REQUEST
    --------------------------------

curl -X POST https://flask-seccomp-container-282247207309.europe-west1.run.app/execute \
-H "Content-Type: application/json" \
-d '{"script": "def main():\n    return {\"message\": \"Hi Alexis ;)!\"}\n"}'

    --------------------------------	
        Issues faced with NsJail
    --------------------------------

Google Cloud Run is a restricted environment where you do not have access to low-level Linux kernel features (in this case : setting namespaces), and NsJail relies on some of these features for sandboxing. 
This is why NsJail is failing with the "Invalid argument" error.


Time to complete the challenge : ~4h

