
# Parameters

    Name :                      gold_small-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     7
    Height :                    7
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
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      18612082371 function calls (18487594632 primitive calls) in 35673.80 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35712.102 35712.102 {built-in method builtins.exec}
                      1    0.876    0.876 35712.101 35712.101 <string>:1(<module>)
                      1   93.534   93.534 35711.226 35711.226 main.py:10(teleport)
                4444128   14.618    0.000 9514.276    0.002 agent.py:26(learn)
                4444128  256.055    0.000 8015.044    0.002 learner.py:42(Qlearn)
                2222064  204.699    0.000 7385.024    0.003 collector.py:36(collect)
               11110320 6373.278    0.001 7156.017    0.001 {built-in method builtins.sum}
                2222064   75.585    0.000 5655.222    0.003 agent.py:50(_learn)
                2222064 3281.428    0.001 5527.281    0.002 replaybuffer.py:27(teleporter_save_data)
                2222064    7.499    0.000 5373.208    0.002 game.py:21(step)
                2222064    9.588    0.000 5038.866    0.002 layers.py:212(step)
        139987666/15554266  515.959    0.000 4235.734    0.000 module.py:866(_call_impl)
                2222064 2666.149    0.001 3965.995    0.002 agent.py:77(interveen)
               11110138   30.145    0.000 3933.582    0.000 network.py:24(forward)
               11110138  124.922    0.000 3836.814    0.000 container.py:117(forward)
                2222064   64.539    0.000 3832.895    0.002 agent.py:101(_learn)
                4444128   34.926    0.000 3117.034    0.001 optimizer.py:84(wrapper)
                2222065  197.426    0.000 3005.667    0.001 layers.py:192(update)
                4444128   18.864    0.000 2958.651    0.001 grad_mode.py:24(decorate_context)
                4444128  117.395    0.000 2900.936    0.001 adam.py:55(step)
                4444128  604.674    0.000 2643.825    0.001 _functional.py:53(adam)
                4443946   99.380    0.000 2621.875    0.001 agent.py:45(__call__)
                4444128   17.196    0.000 2057.986    0.000 tensor.py:195(backward)
                4444128   18.088    0.000 2040.252    0.000 __init__.py:68(backward)
                2222064  149.206    0.000 2008.836    0.001 layers.py:17(step)
                4444128 1939.724    0.000 1939.724    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              223793728 1881.280    0.000 1881.280    0.000 {built-in method clone}
              222206400  215.817    0.000 1841.085    0.000 layer.py:66(move)
                6686497   38.677    0.000 1635.907    0.000 layers.py:233(restart)
               22220276   46.812    0.000 1484.482    0.000 conv.py:398(forward)
                2222064  765.212    0.000 1458.017    0.001 replaybuffer.py:23(sample_data)
               22220276   27.547    0.000 1417.660    0.000 conv.py:390(_conv_forward)
                2222064  856.561    0.000 1394.138    0.001 agent.py:59(modify)
               22220276 1390.114    0.000 1390.114    0.000 {built-in method conv2d}
                6686497    8.580    0.000 1269.112    0.000 levels.py:8(__init__)
                6686497   23.593    0.000 1260.532    0.000 level.py:8(__init__)
                6686497  226.450    0.000 1178.357    0.000 levels.py:11(generate)
               28886286   56.636    0.000 1024.010    0.000 linear.py:93(forward)
               28886286   23.554    0.000  942.389    0.000 functional.py:1737(linear)
               28886286  913.119    0.000  913.119    0.000 {built-in method torch._C._nn.linear}
                2222064   29.688    0.000  848.163    0.000 agent.py:96(__call__)
               13333272   22.907    0.000  827.185    0.000 tensor.py:575(__iter__)
                6666010   37.018    0.000  810.192    0.000 agent.py:54(modify_board)
              222206400  185.766    0.000  800.811    0.000 layers.py:223(isFree)
               13333272  784.000    0.000  784.000    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               17776330  667.762    0.000  667.762    0.000 {built-in method cat}
              782337288  506.880    0.000  615.045    0.000 layer.py:63(isFree)
              222206400  223.643    0.000  602.731    0.000 layers.py:229(check)
               39996424   31.769    0.000  574.036    0.000 activation.py:713(forward)
              222206500   61.370    0.000  569.294    0.000 {built-in method builtins.all}
                8888260  290.302    0.000  547.506    0.000 layer.py:90(update)
                2222064   36.995    0.000  543.498    0.000 replaybuffer.py:19(stacker)
               39996424   32.677    0.000  542.267    0.000 functional.py:1364(leaky_relu)
                6666010  538.192    0.000  538.192    0.000 {built-in method torch._C._nn.one_hot}
              681987549  161.577    0.000  531.739    0.000 layers.py:197(<genexpr>)
               79994304  511.089    0.000  511.089    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               39996424  503.164    0.000  503.164    0.000 {built-in method torch._C._nn.leaky_relu}
                4444128   86.480    0.000  469.396    0.000 optimizer.py:189(zero_grad)
               79994304  460.161    0.000  460.161    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6686497  242.393    0.000  458.606    0.000 levels.py:76(RFS)
                9404228  420.339    0.000  420.339    0.000 {built-in method tensor}
              230459738  400.176    0.000  400.176    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              222206500  233.230    0.000  348.476    0.000 layers.py:65(isDone)
              222206400  212.146    0.000  329.174    0.000 layers.py:50(check)
               26745988   33.428    0.000  318.025    0.000 layer.py:40(restart)
               39997152  301.329    0.000  301.329    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                4444128    4.362    0.000  300.222    0.000 game.py:17(board)
               39997152  262.979    0.000  262.979    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4443946   97.516    0.000  260.562    0.000 exploration.py:53(softmaxer)
               39997152  249.623    0.000  249.623    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               39997152  243.558    0.000  243.558    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               15595058   92.849    0.000  235.106    0.000 random.py:315(sample)
                6686597  106.572    0.000  222.425    0.000 layers.py:37(reset)
              279980118  175.675    0.000  216.765    0.000 tensor.py:906(grad)
              434113085  160.276    0.000  216.125    0.000 layer.py:76(add)
              758678263  145.084    0.000  208.003    0.000 enum.py:646(__hash__)
              879381576  199.065    0.000  199.065    0.000 layer.py:85(elements)
               39997152  185.390    0.000  185.390    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4444128    6.139    0.000  177.087    0.000 loss.py:527(forward)
                4444128   16.042    0.000  170.948    0.000 functional.py:2898(mse_loss)
                6686497   32.787    0.000  161.451    0.000 level.py:34(notUsed)
             1748841793  145.793    0.000  145.793    0.000 layer.py:59(positions)
              206297654   91.909    0.000  135.740    0.000 layer.py:72(remove)
              204769570   90.932    0.000  131.846    0.000 random.py:250(_randbelow_with_getrandbits)
        711385287/711385285   81.273    0.000  111.774    0.000 {built-in method builtins.len}
              213967904   73.229    0.000  109.699    0.000 levels.py:33(<genexpr>)
                4444128  105.992    0.000  105.992    0.000 {built-in method torch._C._nn.mse_loss}
             1426103300  100.997    0.000  100.997    0.000 {method 'append' of 'list' objects}
               22220276   14.269    0.000   97.544    0.000 flatten.py:39(forward)
                4444794   96.560    0.000   96.560    0.000 {built-in method max}
              167162425   93.720    0.000   93.720    0.000 level.py:25(inverse)
                6666192    8.693    0.000   93.006    0.000 tensor.py:525(__rsub__)
                2222064    8.133    0.000   90.876    0.000 exploration.py:47(epsilonGreedy)
              153320938   87.341    0.000   87.341    0.000 {built-in method torch._C._get_tracing_state}
                4443946   83.316    0.000   83.316    0.000 {built-in method multinomial}
               22220276   83.275    0.000   83.275    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6666192   82.872    0.000   82.872    0.000 {built-in method rsub}
                4444128   16.999    0.000   78.783    0.000 __init__.py:28(_make_grads)
                4444128   77.363    0.000   77.363    0.000 {built-in method gather}
               60178473   27.569    0.000   76.629    0.000 random.py:285(choice)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9393238: <gold_small_0> in cluster <dcc> Done

Job <gold_small_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 01:58:30 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 01:58:30 2021
Terminated at Mon Mar  8 11:54:09 2021
Results reported at Mon Mar  8 11:54:09 2021

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

    CPU time :                                   35620.28 sec.
    Max Memory :                                 5414 MB
    Average Memory :                             4010.95 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2778.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35745 sec.
    Turnaround time :                            35739 sec.

The output (if any) is above this job summary.

