from flask import request
from flask_restx import Namespace, Resource, fields
from ..service.utente_escursione_service import get_all_iscrizioni

api = Namespace('iscrizione', description='Azioni relative all\'iscrizione ad una Escursione')

escursione = api.model('escursione', {
    'id_escursione': fields.String(description='user Identifier'),
    'stato': fields.Integer(description='number of friends'),
    # TODO add other fields
})

id_escursione = api.model('id_escursione', {
    'id_escursione': fields.String(description='user Identifier')
})

@api.route('/')
class Iscrizione(Resource):
    @api.doc('Ottieni la lista di tutte le iscrizioni dell\'utente')
    @api.marshal_list_with(escursione)
    @api.expect(None, validate = True)
    def get(self):
        """ Ottieni la lista di tutte le iscrizioni dell'utente """
        return 
    
    @api.doc('Iscrizione utente ad una Escursione')
    @api.expect(id_escursione, validate = True)
    def post(self):
        """ Iscrizione utente ad una Escursione """
        return 
    
    @api.expect(id_escursione, validate = True)
    def delete(self):
        """ Rimozione iscrizione dell'utente """
        return