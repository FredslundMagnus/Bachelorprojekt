
# Parameters

    Name :                      ReTest2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        500000.0
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
    Counterfacts :              1
    Topn :                      5
    Random counterfacts :       True
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      32839076769 function calls (32690635494 primitive calls) in 42907.66 seconds

##    Ordered by: cumulative time
   List reduced from 510 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.663 42907.663 {built-in method builtins.exec}
                      1    3.486    3.486 42907.663 42907.663 <string>:1(<module>)
                      1  199.758  199.758 42904.177 42904.177 main.py:75(CFagent)
                5554437   20.542    0.000 16666.394    0.003 agent.py:29(learn)
                5552823  409.274    0.000 13857.850    0.002 learner.py:42(Qlearn)
                1851479    9.260    0.000 8890.203    0.005 game.py:41(step)
                1851479   11.889    0.000 8458.950    0.005 layers.py:718(step)
                1851479  198.676    0.000 6442.023    0.003 agent.py:54(_learn)
        166979532/18539948  711.653    0.000 6241.307    0.000 module.py:866(_call_impl)
                1851479  196.210    0.000 5958.139    0.003 agent.py:202(_learn)
                5552823   48.341    0.000 5833.724    0.001 optimizer.py:84(wrapper)
               12987125   36.733    0.000 5813.309    0.000 network.py:24(forward)
               12987125  182.363    0.000 5694.339    0.000 container.py:117(forward)
                5552823   23.405    0.000 5603.583    0.001 grad_mode.py:24(decorate_context)
                5552823  168.340    0.000 5525.521    0.001 adam.py:55(step)
                1851479  159.198    0.000 5413.403    0.003 layers.py:17(step)
              184752792  301.579    0.000 5236.438    0.000 layer.py:98(move)
                5552823 1137.773    0.000 5175.337    0.001 _functional.py:53(adam)
                1851479   54.855    0.000 4233.709    0.002 agent.py:117(_learn)
                5552823   23.359    0.000 3494.449    0.001 tensor.py:195(backward)
                5552823   22.406    0.000 3470.269    0.001 __init__.py:68(backward)
                5552823 3322.876    0.001 3322.876    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1851479  390.295    0.000 3078.211    0.002 agent.py:210(counterfact)
                1851480  277.102    0.000 3017.381    0.002 layers.py:684(update)
              184752792  624.609    0.000 2985.665    0.000 layers.py:735(check)
                3714211   98.233    0.000 2733.777    0.001 agent.py:49(__call__)
                1851479 2066.358    0.001 2681.137    0.001 replaybuffer.py:22(sample_data)
                1851479 1264.361    0.001 2613.249    0.001 agent.py:88(interveen)
                1851479 1296.603    0.001 2421.701    0.001 replaybuffer.py:28(teleporter_save_data)
                1851479 1651.016    0.001 2243.104    0.001 replaybuffer.py:52(sample_data)
               24651948 2210.475    0.000 2210.475    0.000 {built-in method tensor}
               20408237   13.836    0.000 2084.114    0.000 game.py:37(board)
               25974250   58.520    0.000 2057.541    0.000 conv.py:398(forward)
               25974250   38.437    0.000 1971.738    0.000 conv.py:390(_conv_forward)
               25974250 1933.301    0.000 1933.301    0.000 {built-in method conv2d}
               29623672  990.266    0.000 1773.458    0.000 layer.py:167(NoRock_update)
              184752792  312.594    0.000 1678.499    0.000 layers.py:729(isFree)
               35258417   71.643    0.000 1641.044    0.000 linear.py:93(forward)
                1851479 1078.339    0.001 1620.192    0.001 agent.py:67(modify)
               35258417   30.663    0.000 1532.566    0.000 functional.py:1737(linear)
               35258417 1494.084    0.000 1494.084    0.000 {built-in method torch._C._nn.linear}
             1400164894 1104.329    0.000 1365.904    0.000 layer.py:95(isFree)
               83427768 1074.364    0.000 1074.364    0.000 {built-in method clone}
              103650544 1056.306    0.000 1056.306    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               24072410 1012.829    0.000 1012.829    0.000 {built-in method cat}
                1849865   33.892    0.000  941.882    0.001 agent.py:171(__call__)
              103650544  926.314    0.000  926.314    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               48245542   39.235    0.000  902.050    0.000 activation.py:713(forward)
                1851479   32.280    0.000  890.404    0.000 agent.py:112(__call__)
               48245542   43.338    0.000  862.815    0.000 functional.py:1364(leaky_relu)
                5565690   41.286    0.000  815.451    0.000 agent.py:59(modify_board)
               48245542  810.885    0.000  810.885    0.000 {built-in method torch._C._nn.leaky_relu}
                5552823  130.984    0.000  808.744    0.000 optimizer.py:189(zero_grad)
                1851479  584.215    0.000  762.163    0.000 replaybuffer.py:58(CF_save_data)
              184752792  410.784    0.000  655.977    0.000 layers.py:246(check)
             2624553463  456.960    0.000  655.090    0.000 enum.py:646(__hash__)
              185123497  156.967    0.000  652.540    0.000 {built-in method builtins.any}
                1875983   19.496    0.000  588.526    0.000 layers.py:740(restart)
               51825272  578.824    0.000  578.824    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              184752792  329.170    0.000  548.836    0.000 layers.py:286(check)
                5565690  521.033    0.000  521.033    0.000 {built-in method torch._C._nn.one_hot}
              185148000   83.495    0.000  517.074    0.000 {built-in method builtins.all}
               51825272  506.890    0.000  506.890    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1649448153  406.236    0.000  495.572    0.000 layers.py:700(<genexpr>)
                1851479   34.494    0.000  479.804    0.000 replaybuffer.py:18(stacker)
               51825272  478.790    0.000  478.790    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               51825272  475.447    0.000  475.447    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1849865   32.571    0.000  463.989    0.000 replaybuffer.py:48(stacker)
              985908118  243.595    0.000  455.150    0.000 layers.py:690(<genexpr>)
              573723439  444.467    0.000  444.467    0.000 layer.py:146(elements)
                1875983   10.937    0.000  416.634    0.000 level.py:8(__init__)
                1851479  230.478    0.000  380.855    0.000 collector.py:46(collect)
               51825272  369.332    0.000  369.332    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             3386073206  354.582    0.000  354.582    0.000 layer.py:91(positions)
                1875983   38.904    0.000  326.388    0.000 levels.py:164(generate)
        4060854647/4060854644  279.462    0.000  315.883    0.000 {built-in method builtins.len}
              362776988  239.081    0.000  297.942    0.000 tensor.py:906(grad)
                7454924  109.562    0.000  292.377    0.000 random.py:315(sample)
                3714211  103.170    0.000  291.844    0.000 exploration.py:53(softmaxer)
               90843323  282.380    0.000  282.380    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              184752792  177.512    0.000  281.744    0.000 layers.py:313(check)
              184752792  174.265    0.000  278.834    0.000 layers.py:273(check)
                1851479   50.792    0.000  272.919    0.000 agent.py:277(counterfact_check)
                5552823    8.282    0.000  270.447    0.000 loss.py:527(forward)
                5552823   21.452    0.000  262.164    0.000 functional.py:2898(mse_loss)
              184752792  161.921    0.000  256.611    0.000 layers.py:48(check)
                3751966   33.955    0.000  236.111    0.000 level.py:41(notUsed)
             2624574886  198.134    0.000  198.134    0.000 {built-in method builtins.hash}
              184752792  127.926    0.000  192.358    0.000 layers.py:23(check)
               12960353  185.410    0.000  185.410    0.000 {built-in method sum}
                5552823  171.979    0.000  171.979    0.000 {built-in method torch._C._nn.mse_loss}
                5553379  154.262    0.000  154.262    0.000 {built-in method max}
               25974250   18.194    0.000  149.844    0.000 flatten.py:39(forward)
               15007864   18.110    0.000  147.413    0.000 layer.py:69(restart)
                3702960  147.086    0.000  147.086    0.000 {built-in method nonzero}
              231209914   98.413    0.000  144.934    0.000 random.py:250(_randbelow_with_getrandbits)
              257772528  105.978    0.000  143.858    0.000 layer.py:130(add)
             1062376613  138.757    0.000  138.757    0.000 layer.py:203(isBlocking)
              162332909   93.873    0.000  137.888    0.000 layer.py:126(remove)
             1675502144  133.866    0.000  133.866    0.000 {method 'random' of '_random.Random' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9512493: <ReTest2_0> in cluster <dcc> Done

Job <ReTest2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 13 13:40:46 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 13 16:45:44 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 16:45:44 2021
Terminated at Wed Apr 14 04:40:56 2021
Results reported at Wed Apr 14 04:40:56 2021

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

    CPU time :                                   42803.02 sec.
    Max Memory :                                 6777 MB
    Average Memory :                             5047.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9607.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42913 sec.
    Turnaround time :                            54010 sec.

The output (if any) is above this job summary.

