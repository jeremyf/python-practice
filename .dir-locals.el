;;; Directory Local Variables            -*- no-byte-compile: t -*-
;;; For more information see (info "(emacs) Directory Variables")

((python-ts-mode . ((venv-location . ~/git/python-practice/.venv/)
                    (eglot-workspace-configuration . (:pylsp
                                                      (:configurationSources
                                                       ["pycodestyle"]
                                                       :plugins
                                                       (:autopep8
                                                        (:enabled t)
                                                        :flake8
                                                        (:config nil :enabled :json-false :exclude
	                                                               []
	                                                               :executable "flake8" :extendIgnore
	                                                               []
	                                                               :filename nil :hangClosing nil :ignore
	                                                               []
	                                                               :indentSize nil :maxComplexity nil :maxLineLength nil :perFileIgnores
	                                                               []
	                                                               :select nil)
                                                        :jedi
                                                        (:auto_import_modules
                                                         ["numpy"]
                                                         :env_vars nil :environment nil :extra_paths
                                                         [])
                                                        :jedi_completion
                                                        (:cache_for
                                                         ["pandas" "numpy" "tensorflow" "matplotlib"]
                                                         :eager :json-false :enabled t :fuzzy :json-false :include_class_objects :json-false :include_function_objects :json-false :include_params t :resolve_at_most 25)
                                                        :jedi_definition
                                                        (:enabled t :follow_builtin_definitions t :follow_builtin_imports t :follow_imports t)
                                                        :jedit_hover
                                                        (:enabled t)
                                                        :jedi_references
                                                        (:enabled t)
                                                        :jedi_signature_help
                                                        (:enabled t)
                                                        :jedi_symbols
                                                        (:all_scopes t :enabled t :include_import_symbols t)
                                                        :mccabe
                                                        (:enabled t :threshold 15)
                                                        :preload
                                                        (:enabled t :modules
	                                                                [])
                                                        :pycodestyle
                                                        (:enabled t :exclude
	                                                                []
	                                                                :filename
	                                                                []
	                                                                :hangClosing nil :ignore
	                                                                []
	                                                                :indentSize nil :maxLineLength nil :select nil)
                                                        :pydocstyle
                                                        (:addIgnore
                                                         []
                                                         :addSelect
                                                         []
                                                         :convention nil :enabled :json-false :ignore
                                                         []
                                                         :match "(?!test_).*\\.py" :matchDir "[^\\.].*" :select nil)
                                                        :pyflakes
                                                        (:enabled t)
                                                        :pylint
                                                        (:args
                                                         []
                                                         :enabled :json-false :executable nil)
                                                        :rope_autoimport
                                                        (:code_actions
                                                         (:enabled t)
                                                         :completions
                                                         (:enabled t)
                                                         :enabled :json-false :memory :json-false)
                                                        :rope_completion
                                                        (:eager :json-false :enabled :json-false)
                                                        :yapf
                                                        (:enabled t))
                                                       :rope
                                                       (:extensionModules nil :ropeFolder nil))))))) ; string array: null (default)
