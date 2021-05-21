
# Parameters

    Name :                      SuperCausal_convert4-0
    Main :                      CFagent
    Level :                     Levels.CausalSuper
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                4
    Counterfacts :              2
    Topn :                      3
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      90125791041 function calls (89807921334 primitive calls) in 86113.60 seconds

##    Ordered by: cumulative time
   List reduced from 512 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.602 86113.602 {built-in method builtins.exec}
                      1    4.211    4.211 86113.602 86113.602 <string>:1(<module>)
                      1  341.194  341.194 86109.391 86109.391 main.py:80(CFagent)
               10117608   39.837    0.000 24346.221    0.002 agent.py:29(learn)
                3372536   13.200    0.000 22589.658    0.007 game.py:42(step)
                3372536   20.275    0.000 21834.036    0.006 layers.py:827(step)
               10117605  620.676    0.000 19855.015    0.002 learner.py:42(Qlearn)
                3372536  289.315    0.000 15574.595    0.005 layers.py:17(step)
              336945913  576.064    0.000 15253.634    0.000 layer.py:106(move)
                3372536  887.210    0.000 15219.055    0.005 agent.py:212(counterfact)
              336945913 1574.494    0.000 11587.814    0.000 layers.py:844(check)
        355598801/37730785 1390.196    0.000 11394.758    0.000 module.py:866(_call_impl)
               27613180   77.560    0.000 10666.129    0.000 network.py:28(forward)
               27613180  348.961    0.000 10414.511    0.000 container.py:117(forward)
                3372536  339.120    0.000 9462.021    0.003 agent.py:54(_learn)
               87301289 8960.173    0.000 8960.173    0.000 {built-in method tensor}
               79543725   43.808    0.000 8791.495    0.000 game.py:38(board)
                3372536  337.166    0.000 8682.909    0.003 agent.py:204(_learn)
               10117605   79.088    0.000 7882.038    0.001 optimizer.py:84(wrapper)
               10117605   42.223    0.000 7514.280    0.001 grad_mode.py:24(decorate_context)
               10117605  299.877    0.000 7380.537    0.001 adam.py:55(step)
               10117605 1550.986    0.000 6743.398    0.001 _functional.py:53(adam)
                3372537  489.736    0.000 6214.775    0.002 layers.py:793(update)
                3372536  100.877    0.000 6141.006    0.002 agent.py:117(_learn)
                8740791  217.547    0.000 5507.987    0.001 agent.py:49(__call__)
              101176080 2707.375    0.000 5127.655    0.000 layer.py:175(NoRock_update)
                3372536 4098.953    0.001 5115.281    0.002 replaybuffer.py:22(sample_data)
               10117605   39.017    0.000 5034.238    0.000 tensor.py:195(backward)
               10117605   37.477    0.000 4993.631    0.000 __init__.py:68(backward)
                3372536 3898.613    0.001 4870.008    0.001 replaybuffer.py:67(sample_data)
               10117605 4761.869    0.000 4761.869    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3372536 1960.018    0.001 4073.899    0.001 agent.py:88(interveen)
                3372536 2191.763    0.001 3917.425    0.001 replaybuffer.py:28(teleporter_save_data)
               55226360  122.596    0.000 3849.971    0.000 conv.py:398(forward)
               55226360   90.404    0.000 3674.145    0.000 conv.py:390(_conv_forward)
               55226360 3583.740    0.000 3583.740    0.000 {built-in method conv2d}
            12540417391 2050.208    0.000 3032.118    0.000 enum.py:646(__hash__)
               76094468  155.838    0.000 2940.136    0.000 linear.py:93(forward)
               76094468   62.260    0.000 2710.062    0.000 functional.py:1737(linear)
                2009715   38.506    0.000 2651.536    0.001 agent.py:176(choose_action)
               76094468 2632.403    0.000 2632.403    0.000 {built-in method torch._C._nn.linear}
              336945913  625.219    0.000 2592.264    0.000 layers.py:838(isFree)
                3372536 1540.788    0.000 2365.027    0.001 agent.py:67(modify)
              336945913 1419.586    0.000 2336.991    0.000 layers.py:734(check)
             3136165102 1577.188    0.000 1967.045    0.000 layer.py:103(isFree)
              336945913 1198.956    0.000 1946.738    0.000 layers.py:717(check)
              336945913 1089.492    0.000 1801.477    0.000 layers.py:700(check)
               45838672 1657.740    0.000 1657.740    0.000 {built-in method cat}
              103707648   91.287    0.000 1571.164    0.000 activation.py:713(forward)
              160847947 1569.524    0.000 1569.524    0.000 {built-in method clone}
               12113327   76.769    0.000 1538.055    0.000 agent.py:59(modify_board)
              342329608  349.860    0.000 1527.445    0.000 {built-in method builtins.any}
              103707648   83.609    0.000 1479.877    0.000 functional.py:1364(leaky_relu)
                3372533   52.517    0.000 1475.238    0.000 agent.py:172(__call__)
                3372536   52.599    0.000 1397.424    0.000 agent.py:112(__call__)
              103707648 1378.606    0.000 1378.606    0.000 {built-in method torch._C._nn.leaky_relu}
              188861956 1318.074    0.000 1318.074    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              931906264 1260.833    0.000 1260.833    0.000 layer.py:154(elements)
            11771422056 1199.719    0.000 1199.719    0.000 layer.py:99(positions)
             3691429896  959.194    0.000 1177.585    0.000 layers.py:809(<genexpr>)
              188861956 1165.391    0.000 1165.391    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10117605  206.635    0.000 1160.272    0.000 optimizer.py:189(zero_grad)
              337253700  143.406    0.000 1137.062    0.000 {built-in method builtins.all}
                1669164   21.822    0.000 1119.762    0.001 layers.py:849(restart)
             1388212639  375.696    0.000 1035.112    0.000 layers.py:799(<genexpr>)
               12113327 1004.385    0.000 1004.385    0.000 {built-in method torch._C._nn.one_hot}
            12540455838  981.917    0.000  981.917    0.000 {built-in method builtins.hash}
                1669164    9.369    0.000  966.555    0.001 level.py:8(__init__)
              336945913  599.261    0.000  964.320    0.000 layers.py:686(check)
              336945913  558.504    0.000  909.355    0.000 layers.py:658(check)
              336945913  555.936    0.000  901.255    0.000 layers.py:672(check)
                1669164   32.406    0.000  872.278    0.001 levels.py:261(generate)
        12470610131/12470610128  752.228    0.000  823.753    0.000 {built-in method builtins.len}
               13703698  134.280    0.000  806.720    0.000 level.py:41(notUsed)
                3372536  664.252    0.000  801.515    0.000 replaybuffer.py:73(CF_save_data)
               94430978  776.821    0.000  776.821    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3372536   61.735    0.000  769.777    0.000 replaybuffer.py:18(stacker)
                3372533   61.501    0.000  735.136    0.000 replaybuffer.py:63(stacker)
               94430978  667.673    0.000  667.673    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               94430978  622.508    0.000  622.508    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               94430978  617.629    0.000  617.629    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              337253700  393.538    0.000  597.042    0.000 layers.py:113(isDone)
                8740791  204.297    0.000  542.428    0.000 exploration.py:53(softmaxer)
              661016930  425.697    0.000  529.402    0.000 tensor.py:906(grad)
                3372536  304.376    0.000  517.076    0.000 collector.py:46(collect)
                2009715  435.158    0.000  510.096    0.000 agent.py:187(convert_values)
                6745072  175.927    0.000  470.586    0.000 random.py:315(sample)
               94430978  469.168    0.000  469.168    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              336945913  304.509    0.000  460.908    0.000 layers.py:646(check)
               10117605   13.195    0.000  422.579    0.000 loss.py:527(forward)
               10117605   37.532    0.000  409.385    0.000 functional.py:2898(mse_loss)
               13703698   11.636    0.000  387.053    0.000 level.py:38(elementsIn)
              176333807  363.237    0.000  363.237    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              336945913  237.258    0.000  356.634    0.000 layers.py:23(check)
              101176080  350.516    0.000  350.516    0.000 layer.py:186(<listcomp>)
             3136165102  329.409    0.000  329.409    0.000 layer.py:211(isBlocking)
             3721769414  308.121    0.000  308.121    0.000 {method 'random' of '_random.Random' objects}
              101176080  302.137    0.000  302.137    0.000 layer.py:187(<listcomp>)
               55226360   40.610    0.000  258.035    0.000 flatten.py:39(forward)
               10117605  253.762    0.000  253.762    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9672992: <SuperCausal_convert4_0> in cluster <dcc> Done

Job <SuperCausal_convert4_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May 20 18:43:27 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 20 18:43:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 20 18:43:28 2021
Terminated at Fri May 21 18:38:54 2021
Results reported at Fri May 21 18:38:54 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85874.95 sec.
    Max Memory :                                 9620 MB
    Average Memory :                             6341.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6764.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86125 sec.
    Turnaround time :                            86127 sec.

The output (if any) is above this job summary.

