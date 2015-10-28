#include <iostream>
#include <string.h>

using namespace std;

/* framework code */
class Document {
    public:
        Document(const char *name) {
            cout << "    ctor of Document" << endl;
            strcpy(_name, name);
        }
        virtual void open() = 0;
        virtual void close() = 0;
        char *get_name() {
            return _name;
        }
    private:
        char _name[20];
};

class Application {
    public:
        Application() {
            cout << "ctor of Application" << endl;
        }
        void new_document(const char *name) {
            cout << "Application::new_document()" << endl;
            _docs[_index] = create_document(name);
            _docs[_index++]->open();
        }
        void report_docs() {
            cout << "Application::report_docs()" << endl;
            for (int i = 0; i < _index; i++) {
                cout << "    " << _docs[i]->get_name() << endl;
            }
        }
        virtual Document *create_document(const char *name) = 0;
    private:
        int _index {};
        Document *_docs[10] {};
};

/* user code */
class MyDocument : public Document {
    public:
        MyDocument(const char *name) : Document(name) {
            cout << "    ctor of MyDocument" << endl;
        }
        void open() {
            cout << "    MyDocument::open()" << endl;
        }
        void close() {
            cout << "    MyDocument::close()" << endl;
        }
};

class MyApplication : public Application {
    public:
        MyApplication() {
            cout << "ctor of MyApplication" << endl;
        }
        Document *create_document(const char *name) {
            cout << "    MyApplication::create_document()" << endl;
            return new MyDocument(name);
        }
};

int main() {
    MyApplication app;

    app.new_document("foo");
    app.new_document("bar");

    app.report_docs();
}
