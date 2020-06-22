@Grab('org.yaml:snakeyaml:1.17')

import org.yaml.snakeyaml.Yaml
import groovy.json.JsonOutput
import groovy.json.JsonSlurper



Yaml parser = new Yaml()
manifest = parser.load(('testdata.yaml' as File).text)

// test.each{ println it.subject }

testmap = ["key1": 3, "leonardo": ["nested map": "bwammm"]]
println JsonOutput.toJson(testmap)

def jsonSlurper = new JsonSlurper()
objectrep = jsonSlurper.parseText """
    {"name":"national-records-testdata","image":"docker-registry.default.svc:5000/default/national-record-and-profile-management-testdata:da53b6a04bf5a439dea78876eb2e2ff487cec6d2","env":[{"name":"POSTGRESQL_USERNAME","valueFrom":{"secretKeyRef":{"name":"postgresql-nationalrecord-secrets","key":"database-user"}}},{"name":"POSTGRESQL_PASSWORD","valueFrom":{"secretKeyRef":{"name":"postgresql-nationalrecord-secrets","key":"database-password"}}},{"name":"POSTGRESQL_URL","value":"jdbc:postgresql://postgresql:5432/nationalrecord"}],"resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","imagePullPolicy":"IfNotPresent"}
    """
jsonrep = JsonOutput.toJson(objectrep)

map = manifest.annotations['pod.alpha.kubernetes.io/init-containers']
    // map = '[{"name":"national-records-testdata","image":"docker-registry.default.svc:5000/default/national-record-and-profile-management-testdata:da53b6a04bf5a439dea78876eb2e2ff487cec6d2","env":[{"name":"POSTGRESQL_USERNAME","valueFrom":{"secretKeyRef":{"name":"postgresql-nationalrecord-secrets","key":"database-user"}}},{"name":"POSTGRESQL_PASSWORD","valueFrom":{"secretKeyRef":{"name":"postgresql-nationalrecord-secrets","key":"database-password"}}},{"name":"POSTGRESQL_URL","value":"jdbc:postgresql://postgresql:5432/nationalrecord"}],"resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","imagePullPolicy":"IfNotPresent"}]'
map = jsonSlurper.parseText(map)
map[0]['name'] = "CHANGE PLACES"
map = JsonOutput.toJson(map)
println """$map"""
// println """[$map]"""



 