
# Parameters

    Name :                      ReTest12-0
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65052796465 function calls (64815445522 primitive calls) in 86116.85 seconds

##    Ordered by: cumulative time
   List reduced from 504 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.847 86116.847 {built-in method builtins.exec}
                      1    4.036    4.036 86116.847 86116.847 <string>:1(<module>)
                      1  309.360  309.360 86112.811 86112.811 main.py:75(CFagent)
                8841165   36.663    0.000 31376.627    0.004 agent.py:29(learn)
                8839694  719.363    0.000 26450.914    0.003 learner.py:42(Qlearn)
                2947055   14.746    0.000 17662.309    0.006 game.py:41(step)
                2947055   17.613    0.000 16888.046    0.006 layers.py:718(step)
                2947055  100.674    0.000 12085.559    0.004 agent.py:54(_learn)
                2947055  262.365    0.000 11434.086    0.004 layers.py:17(step)
                8839694   51.450    0.000 11372.561    0.001 grad_mode.py:23(decorate_context)
        266950402/29601150 1034.341    0.000 11280.371    0.000 module.py:715(_call_impl)
                2947055  101.441    0.000 11250.541    0.004 agent.py:202(_learn)
                8839694  305.981    0.000 11221.201    0.001 adam.py:55(step)
              292416758  812.453    0.000 11147.291    0.000 layer.py:98(move)
               20761456   49.659    0.000 10564.953    0.001 network.py:27(forward)
               20761456  271.135    0.000 10389.863    0.001 container.py:115(forward)
                8839694 2066.405    0.000 9668.152    0.001 functional.py:53(adam)
                2947055 1650.391    0.001 8287.527    0.003 agent.py:210(counterfact)
                2947055   81.148    0.000 7985.035    0.003 agent.py:117(_learn)
              292416758 1288.401    0.000 6860.442    0.000 layers.py:735(check)
                8839694   51.005    0.000 6047.261    0.001 tensor.py:181(backward)
                8839694   33.020    0.000 5996.256    0.001 __init__.py:68(backward)
                8839694 5737.571    0.001 5737.571    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2947056  414.946    0.000 5410.417    0.002 layers.py:684(update)
               49352999 5372.229    0.000 5372.229    0.000 {built-in method tensor}
                2947055 3801.429    0.001 5177.969    0.002 replaybuffer.py:22(sample_data)
               42533741   25.983    0.000 5147.027    0.000 game.py:37(board)
                2947055 2532.316    0.001 4954.167    0.002 agent.py:88(interveen)
                5958142  144.168    0.000 4888.442    0.001 agent.py:49(__call__)
                2947055 2509.770    0.001 4881.700    0.002 replaybuffer.py:28(teleporter_save_data)
                2947055 3351.706    0.001 4710.091    0.002 replaybuffer.py:52(sample_data)
               41522912   67.572    0.000 3736.946    0.000 conv.py:422(forward)
               41522912   82.327    0.000 3638.583    0.000 conv.py:414(_conv_forward)
               58941110 2105.405    0.000 3625.358    0.000 layer.py:151(update)
               41522912 3541.720    0.000 3541.720    0.000 {built-in method conv2d}
               56390258  127.286    0.000 3410.534    0.000 linear.py:92(forward)
               56390258  212.827    0.000 3222.121    0.000 functional.py:1669(linear)
                2947055 1609.027    0.001 3132.823    0.001 agent.py:67(modify)
              292416758  558.679    0.000 2929.073    0.000 layers.py:729(isFree)
                2947055 1635.695    0.001 2509.749    0.001 replaybuffer.py:58(CF_save_data)
               38368392 2483.432    0.000 2483.432    0.000 {built-in method cat}
              167180125 2405.281    0.000 2405.281    0.000 {built-in method clone}
             2602211724 1970.725    0.000 2370.395    0.000 layer.py:95(isFree)
              577519894 1502.965    0.000 2359.297    0.000 tensor.py:933(grad)
               56390258 2295.840    0.000 2295.840    0.000 {built-in method addmm}
                8839694  214.998    0.000 2294.476    0.000 optimizer.py:167(zero_grad)
              165005660 2049.292    0.000 2049.292    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1115380429  577.503    0.000 1947.637    0.000 {built-in method builtins.any}
              165005660 1702.397    0.000 1702.397    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2945584   47.609    0.000 1678.479    0.001 agent.py:171(__call__)
                2947055   49.195    0.000 1567.436    0.001 agent.py:112(__call__)
               77151714   62.161    0.000 1558.027    0.000 activation.py:713(forward)
               77151714   95.381    0.000 1495.866    0.000 functional.py:1292(leaky_relu)
                8905197   62.358    0.000 1446.726    0.000 agent.py:59(modify_board)
             5463346479 1015.589    0.000 1413.432    0.000 enum.py:646(__hash__)
               77151714 1391.448    0.000 1391.448    0.000 {built-in method torch._C._nn.leaky_relu}
               29612987  160.036    0.000 1210.682    0.000 tensor.py:21(wrapped)
                2947055   51.598    0.000 1170.350    0.000 replaybuffer.py:18(stacker)
                2945584   49.382    0.000 1156.748    0.000 replaybuffer.py:48(stacker)
              746025514  395.801    0.000 1150.202    0.000 overrides.py:1070(has_torch_function)
               82502830 1099.302    0.000 1099.302    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              292416758  823.279    0.000 1076.007    0.000 layers.py:77(check)
              292416758  678.431    0.000 1047.321    0.000 layers.py:246(check)
               82502830 1004.411    0.000 1004.411    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              292416758  567.174    0.000  945.020    0.000 layers.py:286(check)
             3215720343  776.409    0.000  943.087    0.000 layers.py:700(<genexpr>)
              324318587  162.669    0.000  941.143    0.000 {built-in method builtins.all}
                8905197  910.773    0.000  910.773    0.000 {built-in method torch._C._nn.one_hot}
               82502830  906.608    0.000  906.608    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              919970372  844.698    0.000  844.698    0.000 layer.py:146(elements)
                2367387   28.273    0.000  841.723    0.000 layers.py:740(restart)
               82502830  813.781    0.000  813.781    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             1734420313  442.928    0.000  792.671    0.000 layers.py:690(<genexpr>)
              179030906  738.394    0.000  738.394    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2947055  418.261    0.000  700.338    0.000 collector.py:46(collect)
               82502830  640.463    0.000  640.463    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             7290240612  632.640    0.000  632.640    0.000 layer.py:91(positions)
                2367387   14.004    0.000  600.426    0.000 level.py:8(__init__)
              292416758  450.576    0.000  579.931    0.000 layers.py:62(check)
        7101681570/7101681567  432.727    0.000  541.840    0.000 {built-in method builtins.len}
                5958142  187.450    0.000  534.326    0.000 exploration.py:53(softmaxer)
              292416758  325.679    0.000  495.643    0.000 layers.py:273(check)
                8839694   11.343    0.000  491.206    0.000 loss.py:445(forward)
                2947055   89.252    0.000  483.797    0.000 agent.py:277(counterfact_check)
                8839694   47.533    0.000  479.863    0.000 functional.py:2637(mse_loss)
                2367387   79.488    0.000  474.338    0.000 levels.py:199(generate)
               56390258  469.847    0.000  469.847    0.000 {method 't' of 'torch._C._TensorBase' objects}
              292416758  291.550    0.000  460.491    0.000 layers.py:313(check)
               20629385  456.414    0.000  456.414    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               10628884  163.577    0.000  433.282    0.000 random.py:315(sample)
             1578053678  334.637    0.000  421.700    0.000 overrides.py:1083(<genexpr>)
             5463380110  397.848    0.000  397.848    0.000 {built-in method builtins.hash}
              292416758  268.651    0.000  393.969    0.000 layers.py:48(check)
                5893829  384.613    0.000  384.613    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
               20629385  326.367    0.000  326.367    0.000 {built-in method sum}
                4734774   37.481    0.000  321.977    0.000 level.py:41(notUsed)
                8839694  303.931    0.000  303.931    0.000 {built-in method torch._C._nn.mse_loss}
              292416758  202.126    0.000  298.830    0.000 layers.py:23(check)
              261481031  221.276    0.000  291.623    0.000 layer.py:126(remove)
               41522912   29.463    0.000  278.589    0.000 flatten.py:39(forward)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9515003: <ReTest12_0> in cluster <dcc> Done

Job <ReTest12_0> was submitted from host <n-62-30-6> by user <s183905> in cluster <dcc> at Wed Apr 14 13:56:06 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 15 14:39:17 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 15 14:39:17 2021
Terminated at Fri Apr 16 14:34:42 2021
Results reported at Fri Apr 16 14:34:42 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85891.84 sec.
    Max Memory :                                 3298 MB
    Average Memory :                             3273.53 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13086.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            175116 sec.

The output (if any) is above this job summary.

