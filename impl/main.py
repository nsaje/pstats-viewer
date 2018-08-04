import snakeviz.templates
import snakeviz.stats
import tornado.template

# with open(os.path.join(templates.__path__._path[0], 'viz.html')) as f:
#     t = tornado.template.Template(f.read())

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }
