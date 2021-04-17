Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 61, in teleport
    collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/save.py", line 34, in path
    os.mkdir("/".join(path))
FileExistsError: [Errno 17] File exists: 'outputs/causal3_9x9/Teleporter'


# Parameters

    Name :                      causal3_9x9-0
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.04
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      39576068429 function calls (39410771166 primitive calls) in 42911.42 seconds

##    Ordered by: cumulative time
   List reduced from 476 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42911.417 42911.417 {built-in method builtins.exec}
                      1    0.000    0.000 42911.417 42911.417 <string>:1(<module>)
                      1  132.056  132.056 42911.417 42911.417 main.py:43(teleport)
                5903914   18.704    0.000 12627.781    0.002 agent.py:27(learn)
                2951957   11.086    0.000 12216.605    0.004 game.py:27(step)
                2951957   15.176    0.000 11594.792    0.004 layers.py:475(step)
                5903914  337.751    0.000 10602.215    0.002 learner.py:42(Qlearn)
                2951957   97.980    0.000 7593.882    0.003 agent.py:51(_learn)
                2951957  220.968    0.000 7543.439    0.003 layers.py:18(step)
              295195700  350.067    0.000 7298.988    0.000 layer.py:76(move)
                2951957 3790.516    0.001 6436.768    0.002 replaybuffer.py:27(teleporter_save_data)
        185959498/20662638  692.777    0.000 5646.550    0.000 module.py:866(_call_impl)
               14758724   41.776    0.000 5242.911    0.000 network.py:24(forward)
               14758724  165.399    0.000 5113.673    0.000 container.py:117(forward)
                2951957   83.047    0.000 5003.141    0.002 agent.py:110(_learn)
              295195700  693.057    0.000 4387.936    0.000 layers.py:492(check)
                2951957 2653.057    0.001 4374.424    0.001 agent.py:81(interveen)
                5903914   46.199    0.000 4077.936    0.001 optimizer.py:84(wrapper)
                2951958  298.933    0.000 4015.457    0.001 layers.py:446(update)
                5903914   23.091    0.000 3870.944    0.001 grad_mode.py:24(decorate_context)
                5903914  152.426    0.000 3792.510    0.001 adam.py:55(step)
                5902853  136.686    0.000 3520.427    0.001 agent.py:46(__call__)
                2951957 2511.181    0.001 3471.921    0.001 replaybuffer.py:23(sample_data)
                5903914  796.624    0.000 3456.679    0.001 _functional.py:53(adam)
                5903914   22.006    0.000 2758.583    0.000 tensor.py:195(backward)
                5903914   21.800    0.000 2735.740    0.000 __init__.py:68(backward)
                5903914 2606.769    0.000 2606.769    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              295195700  466.396    0.000 2224.464    0.000 layers.py:486(isFree)
              268612048 2189.690    0.000 2189.690    0.000 {built-in method clone}
               29517448   62.368    0.000 1929.059    0.000 conv.py:398(forward)
               29517448   36.914    0.000 1839.776    0.000 conv.py:390(_conv_forward)
               29517448 1802.861    0.000 1802.861    0.000 {built-in method conv2d}
                2951957 1066.174    0.000 1783.367    0.001 agent.py:63(modify)
             2425081808 1425.830    0.000 1758.068    0.000 layer.py:73(isFree)
               26567622  925.040    0.000 1643.102    0.000 layer.py:137(NoRock_update)
               38372258   73.553    0.000 1425.955    0.000 linear.py:93(forward)
               38372258   29.551    0.000 1317.887    0.000 functional.py:1737(linear)
               38372258 1281.335    0.000 1281.335    0.000 {built-in method torch._C._nn.linear}
                4644417   46.223    0.000 1239.433    0.000 layers.py:496(restart)
                2951957   39.297    0.000 1090.337    0.000 agent.py:105(__call__)
                8854810   51.870    0.000 1075.536    0.000 agent.py:55(modify_board)
             4399033771  732.258    0.000 1027.451    0.000 enum.py:646(__hash__)
               26566552  915.347    0.000  915.347    0.000 {built-in method cat}
              295195700  560.118    0.000  903.203    0.000 layers.py:302(check)
               12195009  893.959    0.000  893.959    0.000 {built-in method tensor}
              295195700  514.291    0.000  852.862    0.000 layers.py:261(check)
                4644417   22.451    0.000  795.183    0.000 level.py:8(__init__)
               53130982   45.122    0.000  756.577    0.000 activation.py:713(forward)
                2951957   53.653    0.000  756.273    0.000 replaybuffer.py:19(stacker)
                5903914    6.012    0.000  740.750    0.000 game.py:23(board)
              295195800   80.584    0.000  724.666    0.000 {built-in method builtins.all}
                8854810  712.195    0.000  712.195    0.000 {built-in method torch._C._nn.one_hot}
               53130982   41.502    0.000  711.455    0.000 functional.py:1364(leaky_relu)
                4644417  115.885    0.000  688.223    0.000 levels.py:163(generate)
              906586532  203.618    0.000  676.680    0.000 layers.py:452(<genexpr>)
               53130982  661.726    0.000  661.726    0.000 {built-in method torch._C._nn.leaky_relu}
              106270452  660.452    0.000  660.452    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5903914  108.263    0.000  606.488    0.000 optimizer.py:189(zero_grad)
              106270452  596.740    0.000  596.740    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              295195700  403.743    0.000  555.255    0.000 layers.py:63(check)
              277466858  511.885    0.000  511.885    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              295195700  312.667    0.000  485.421    0.000 layers.py:328(check)
             5770872155  483.424    0.000  483.424    0.000 layer.py:69(positions)
             1211997497  470.364    0.000  470.364    0.000 layer.py:116(elements)
                9288834   56.797    0.000  458.947    0.000 level.py:41(notUsed)
              295195800  300.615    0.000  447.812    0.000 layers.py:110(isDone)
              295195700  282.030    0.000  442.604    0.000 layers.py:287(check)
                2951957  238.865    0.000  409.874    0.000 collector.py:54(collect)
               53135226  405.467    0.000  405.467    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               41799753   53.193    0.000  385.023    0.000 layer.py:50(restart)
              295195700  258.179    0.000  381.303    0.000 layers.py:47(check)
                5902853  132.336    0.000  355.808    0.000 exploration.py:53(softmaxer)
               53135226  344.567    0.000  344.567    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               53135226  320.603    0.000  320.603    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               53135226  319.548    0.000  319.548    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              581248355  218.660    0.000  298.728    0.000 layer.py:100(add)
             4399055106  295.196    0.000  295.196    0.000 {built-in method builtins.hash}
              371946636  228.834    0.000  284.965    0.000 tensor.py:906(grad)
               12240791   98.698    0.000  259.280    0.000 random.py:315(sample)
                5903914    7.990    0.000  238.738    0.000 loss.py:527(forward)
               53135226  237.667    0.000  237.667    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              322467783  152.168    0.000  234.259    0.000 layer.py:96(remove)
              195068524  231.476    0.000  231.476    0.000 level.py:32(inverse)
                5903914   20.946    0.000  230.748    0.000 functional.py:2898(mse_loss)
        2779117516/2779117514  190.268    0.000  229.349    0.000 {built-in method builtins.len}
                4644517  110.514    0.000  220.690    0.000 layers.py:33(reset)
             1885771514  179.433    0.000  179.433    0.000 layer.py:177(isBlocking)
               17711742  178.650    0.000  178.650    0.000 {built-in method sum}
              225017842   98.229    0.000  143.346    0.000 random.py:250(_randbelow_with_getrandbits)
                5903914  141.523    0.000  141.523    0.000 {built-in method torch._C._nn.mse_loss}
             1901743957  140.956    0.000  140.956    0.000 {method 'append' of 'list' objects}
                9288834    8.351    0.000  132.717    0.000 level.py:38(elementsIn)
                5904799  128.755    0.000  128.755    0.000 {built-in method max}
               29517448   18.411    0.000  128.290    0.000 flatten.py:39(forward)
                8855871   11.843    0.000  123.356    0.000 tensor.py:525(__rsub__)
                5902853  110.377    0.000  110.377    0.000 {built-in method multinomial}
               29517448  109.879    0.000  109.879    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                8855871  109.448    0.000  109.448    0.000 {built-in method rsub}
                2951957   11.372    0.000  104.639    0.000 exploration.py:47(epsilonGreedy)
                5903914   21.140    0.000  102.626    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9458194: <causal3_9x9_0> in cluster <dcc> Done

Job <causal3_9x9_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 01:18:04 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 01:18:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 01:18:05 2021
Terminated at Thu Mar 25 13:13:29 2021
Results reported at Thu Mar 25 13:13:29 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
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

    CPU time :                                   42802.82 sec.
    Max Memory :                                 6712 MB
    Average Memory :                             4873.04 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1480.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42947 sec.
    Turnaround time :                            42925 sec.

The output (if any) is above this job summary.

