<h3>Summary:</h3>
<p>Yesterday at 10 AM, an alert was received from monitoring tools indicating "high CPU usage causing more background process launches" on web server 1. This persisted for 45 minutes, impacting server performance and potentially leading to downtime or delayed content delivery.</p>
<h3>Timeline:</h3>
<pre>
<p>Issue detected within 5 minutes.</p>
<p>Alert received via monitoring tools, prompting customer support contact.</p>
<p>Actions taken: Logged into the server to inspect running processes and their resource usage for debugging.</p>
<p>DevOps team took charge of addressing the problem.</p>
<p>Temporary resolution achieved by reducing CPU usage.</p>
</pre>
<h3>Details:</h3>
<p>The alert indicat cpu usage but when devops team check all stuff their found also ram and disk space for server, first the team search for cache files to reduce space of disk then their use “top” command to find usage of cpu and ram after that look at processes and check every process to kill it if no need
.</p>
<h3>the team give corrective and preventive solution:</h3>
<pre><p>advised that vertical scaling is needed for a long-term solution.</p>
<p>Add monitoring metric for cache and disk space</p></pre>
