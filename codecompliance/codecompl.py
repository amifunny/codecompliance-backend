from pathlib import Path
from textwrap import dedent
import sqlite3

from codecompliance import app

def initialize_db(path: Path):
    db = sqlite3.connect(path)

    # Journal Domains (e.g. Computer Science, Biology, ...)
    db.execute(dedent('''
        create table if not exists Domains (
            id integer primary key,
            name text
        );
    '''))

    db.execute(dedent('''
        create table if not exists Journals (
            id integer primary key,
            title text,
            url text,
            issn text
        );
    '''))

    # Many-To-Many connection from Journals to Domains
    db.execute(dedent('''
        create table if not exists JournalsToDomains (
            journal_id integer,
            domain_id integer,
            foreign key (journal_id) references Journals(id),
            foreign key (domain_id) references Domains(id)
        );
    '''))

    # Which policies each journal does have and enforces or not.
    db.execute(dedent('''
        create table if not exists Policies (
            id integer primary key,
            title text,
            first_year text,
            last_year text
        );
    '''))

    # PolicyTypes are meant to represent, for example:
    # - "Restriction" (for "Must be" policies, such as License restrictions)
    # - "Enforcement" (for "Would be good to be" policies, such as having unit tests)
    # - Some custom type, if needed.
    db.execute(dedent('''
        create table if not exists PolicyTypes (
            id integer primary key,
            name text
        );
    '''))

    db.execute(dedent('''
        create table if not exists JournalRatings (
            id integer primary key,
            rating text,
            date text
        );
    '''))


STUB_PAGE_MESSAGE = dedent('''
    Nothing here yet.<br>

    Wanna implement this API function? Submit a PR to <a
    href="https://github.com/codeisscience/codecompliance-backend">the Github
    repo</a>!
    ''')


@app.route('/', methods=['GET'])
def root():
    return dedent('''
        <h1>Code Compliance API</h1>

        Try and check one of these links:
        <ul>
            <li><a href="/journals">Journal listing</a> (WIP)</li>
        </ul>
    ''')


@app.route('/journals', methods=['GET'])
def list_journals():
    '''Lists journals. May receive filters in query parameters.'''
    # TODO: Use `flask.requests.args` to fetch parameters for:
    #       - ?keywords=a,b      (comma-separated keyword list)
    #       - ?keywordcat=code   (specific keyword category)
    return STUB_PAGE_MESSAGE


@app.route('/journals/<identifier>', methods=['GET'])
def list_journal(identifier):
    '''Lists general information from a journal, including its domains'''
    return STUB_PAGE_MESSAGE


@app.route('/journals/<identifier>/policies', methods=['GET'])
def list_journal_policies():
    '''Lists the policies from a journal.'''
    return STUB_PAGE_MESSAGE

